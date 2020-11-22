from django import forms
from django.contrib.auth import get_user_model, password_validation, authenticate
from django.contrib.auth.forms import UserCreationForm
import user_profile.widgets as custom_widgets
from MLModule.Recognize import convert_and_save
import os

User = get_user_model()
path_file = 'temp/'


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'placeholder': 'username',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'placeholder': 'password'
    }))


class SpeechFaceLoginForm(forms.Form):
    speech_path = forms.CharField(widget=custom_widgets.VoiceRecordForm(), label='Speech')

    picture_1 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 1'
    }))

    def save_base64_as_file(self, user_id):

        tmp_path_1 = None
        tmp_path_2 = None
        if self.cleaned_data.get('speech_path') is not '':
            tmp_path_1 = os.path.join(path_file, "speech/User.{0}.{1}.wav".format(user_id, "1"))
            convert_and_save(
                self.cleaned_data.get('speech_path'),
                tmp_path_1
            )

        if self.cleaned_data.get('picture_1') is not '':
            tmp_path_2 = os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "1"))

            convert_and_save(
                self.cleaned_data.get('picture_1'),
                tmp_path_2
            )
        return tmp_path_1, tmp_path_2


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        # 'placeholder': 'username',
    }), required=True)

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'first_name',
        # 'placeholder': 'username',
    }), required=True)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'last_name',
        # 'placeholder': 'username',
    }), required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }), required=True)

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password,', 'class': 'form-control'}),
        strip=False,
    )

    def clean(self):
        super()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Username is taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'gmail.com' not in email:
            raise forms.ValidationError('Email has to be gmail.com')

        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is taken')

        return email

