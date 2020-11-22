import os

from django import forms
from django.contrib.auth import get_user_model

import user_profile.widgets as custom_widgets
from MLModule.Recognize import convert_and_save

User = get_user_model()
path_file = 'data/'


class UserProfile(forms.Form):

    speech_path = forms.CharField(widget=custom_widgets.VoiceRecordForm(), label='Speech')


    picture_1 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 1'
    }))

    picture_2 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 2'
    }), required=False)

    picture_3 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 3'
    }), required=False)

    picture_4 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 4'
    }), required=False)

    picture_5 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 5'
    }), required=False)

    picture_6 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 6'
    }), required=False)

    picture_7 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 7'
    }), required=False)

    picture_8 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 8'
    }), required=False)

    picture_9 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 9'
    }), required=False)

    picture_10 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 8'
    }), required=False)

    picture_11 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 11'
    }), required=False)

    picture_12 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 12'
    }), required=False)

    picture_13 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 13'
    }), required=False)

    picture_14 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 14'
    }), required=False)

    picture_15 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 15'
    }), required=False)

    picture_16 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 16'
    }), required=False)

    picture_17 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 17'
    }), required=False)

    picture_18 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 18'
    }), required=False)

    picture_19 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 19'
    }), required=False)

    picture_20 = forms.CharField(widget=custom_widgets.CameraForm(attrs={
        'label': 'Picture 20'
    }), required=False)

    def save_base64_as_file(self, user_id):

        if self.cleaned_data.get('speech_path') is not '':
            convert_and_save(
                self.cleaned_data.get('speech_path'),
                os.path.join(path_file, "speech/User.{0}.{1}.wav".format(user_id, "1"))
            )

        if self.cleaned_data.get('picture_1') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_1'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "1"))
            )

        if self.cleaned_data.get('picture_2') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_2'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "2"))
            )

        if self.cleaned_data.get('picture_3') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_3'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "3"))
            )

        if self.cleaned_data.get('picture_3') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_3'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "3"))
            )

        if self.cleaned_data.get('picture_3') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_3'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "3"))
            )

        if self.cleaned_data.get('picture_4') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_4'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "4"))
            )

        if self.cleaned_data.get('picture_5') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_5'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "5"))
            )

        if self.cleaned_data.get('picture_6') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_6'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "6"))
            )

        if self.cleaned_data.get('picture_7') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_7'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "7"))
            )

        if self.cleaned_data.get('picture_8') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_8'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "8"))
            )

        if self.cleaned_data.get('picture_9') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_9'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "9"))
            )

        if self.cleaned_data.get('picture_10') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_10'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "10"))
            )

        if self.cleaned_data.get('picture_11') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_11'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "11"))
            )

        if self.cleaned_data.get('picture_12') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_12'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "12"))
            )

        if self.cleaned_data.get('picture_13') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_13'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "13"))
            )

        if self.cleaned_data.get('picture_14') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_14'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "14"))
            )

        if self.cleaned_data.get('picture_15') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_15'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "15"))
            )

        if self.cleaned_data.get('picture_16') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_16'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "16"))
            )

        if self.cleaned_data.get('picture_17') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_17'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "17"))
            )

        if self.cleaned_data.get('picture_18') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_18'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "18"))
            )

        if self.cleaned_data.get('picture_19') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_19'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "19"))
            )

        if self.cleaned_data.get('picture_20') is not '':
            convert_and_save(
                self.cleaned_data.get('picture_20'),
                os.path.join(path_file, "face/User.{0}.{1}.jpeg".format(user_id, "20"))
            )
