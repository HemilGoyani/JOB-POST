# users/forms.py
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'position', 'phone', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autofocus": True}),
    )


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'position', 'phone']