from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login, logout

from free_face_reg_com.form import LoginForm, RegisterForm, SpeechFaceLoginForm
from user_profile.form import UserProfile
from MLModule import Recognize

from google_form.models import GoogleForm

User = get_user_model()
recognize_face = Recognize.Face()
recognize_speech = Recognize.Speech('data/speech/')


def user_logout(request):
    if request.user.is_authenticated:
        print(1)
        logout(request)
    return render(request, 'page/home_page.html', {
        'title': 'Face and Speech Recognize'
    })


def home_page(request):

    if request.user.is_authenticated:
        google_form = GoogleForm.objects.all().last()
        context = {
            'title': 'Face and Speech Recognize',
            'google_form': google_form
        }
        return render(request, 'page/user_page.html', context)

    context = {
        'title': 'Face and Speech Recognize'
    }
    return render(request, 'page/home_page.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    face_speech_form = SpeechFaceLoginForm(request.POST or None)
    context = {
        'title': 'Login',
        'form': form,
        'face_speech_form': face_speech_form
    }

    if request.method == 'POST':
        if face_speech_form.is_valid():
            path_1, path_2 = face_speech_form.save_base64_as_file('temp')
            face_id, conf1 = recognize_face.recognize(path_2)
            speech_id, conf2 = recognize_speech.recognize(path_1)

            face_score = (100 - conf1)
            speech_score = (100 + conf2)
            total_score = ((100 - conf1) + (100 + conf2)) / 2

            if (100 - conf1) + (100 + conf2)/2 >= 60 and face_id == int(speech_id):
                print('OK it {0}'.format(face_id))

                user = User.objects.filter(id=face_id)
                print(user)
                if user is not None:
                    login(request, user[0])

                return render(request, 'page/auth/login_success.html', {
                    'username_login': False,
                    'face_score': face_score,
                    'speech_score': speech_score,
                    'total_score': total_score
                })
            else:
                return render(request, 'page/auth/login_fail.html', {
                    'username_login': False,
                    'face_score': face_score,
                    'speech_score': speech_score,
                    'total_score': total_score
                })

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login_context = {'username_login': True}
            if user is not None:
                login(request, user)
                return render(request, 'page/auth/login_success.html', login_context)
            else:
                return render(request, 'page/auth/login_fail.html', login_context)

    return render(request, 'page/auth/login.html', context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    form_extend = UserProfile(request.POST or None)
    context = {
        'title': 'Register',
        'form': form,
        'form_extend': form_extend
    }

    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()

            if form_extend.is_valid():
                print(form_extend.cleaned_data)
                form_extend.save_base64_as_file(new_user.id)
                recognize_face.generate_training_model('data/face/')
                recognize_speech.train()
                return render(request, 'page/auth/success.html', {})

    return render(request, 'page/auth/register.html', context)
