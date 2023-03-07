from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from string import ascii_letters
from .models import *


class AutoModelsPostForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model_add'].empty_label = "None"

    class Meta:
        model = AutoModels
        fields = ['articles', 'group', 'subgroup', 'photo', 'vendor', 'slug', 'model_add']
        widgets = {
            'articles': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_articles(self):
        articles = self.cleaned_data['articles']
        if not all(map(lambda c: c in ascii_letters, articles)):
            raise ValidationError('word too long')

        return articles


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widget = {
            'first_name': forms.TextInput,
            'last_name': forms.TextInput,
            'username': forms.TextInput,
            'password1': forms.PasswordInput,
            'password2': forms.PasswordInput,
            'email': forms.EmailInput
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput())
    password = forms.CharField(label='Login', widget=forms.PasswordInput())


class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()
