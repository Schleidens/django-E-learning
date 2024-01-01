from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput

from django.contrib.auth import get_user_model

from .models import teacherProfile


class editUserAccountInformationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'profile_picture']

        # specify widget for each input
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control'
            }),

            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),

            'last_name': TextInput(attrs={
                'class': 'form-control'
            }),

            'profile_picture': ClearableFileInput(attrs={
                'multiple': False,
                'class': 'form-control'
            })
        }


class editTeacherProfileForm(forms.ModelForm):

    class Meta:
        model = teacherProfile
        fields = ['bio', 'qualifications', 'title']

        # specify widget for each input
        widgets = {
            'bio': Textarea(attrs={
                'class': 'form-control'
            }),

            'qualifications': TextInput(attrs={
                'class': 'form-control'
            }),

            'title': TextInput(attrs={
                'class': 'form-control'
            }),
        }


class deleteAccountForm(forms.Form):
    delete_profile = forms.BooleanField(widget=forms.HiddenInput, initial=True)
