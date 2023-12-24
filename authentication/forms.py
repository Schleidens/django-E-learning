from django import forms
from django.forms import TextInput, EmailInput, CheckboxInput

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import PasswordChangeForm


class createUserForm(UserCreationForm):
    # specify password for having access to his widget
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    is_teacher = forms.BooleanField(
        required=False,
        label='Are you a teacher ? ',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'is_teacher']

        # add widgets for fields from user_model
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control'
            }),

            'email': EmailInput(attrs={
                'class': 'form-control'
            }),

            'first_name': TextInput(attrs={
                'class': 'form-control'
            }),

            'last_name': TextInput(attrs={
                'class': 'form-control'
            })
        }


# signin user form

class signInUserForm(forms.Form):
    username = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Username'
    )

    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Password'
    )


class changePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(changePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your old password'})
        self.fields['new_password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your new password'})
        self.fields['new_password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm your new password'})
