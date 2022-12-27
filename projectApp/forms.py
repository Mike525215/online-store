from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Username...', 'class': 'input_form'}))
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Password...', 'class': 'input_form'}))
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password...', 'class': 'input_form'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Username...', 'class': 'input_form'}))
    password = forms.CharField(max_length=32, widget=forms.PasswordInput(attrs={'placeholder': 'Password...', 'class': 'input_form'}))
    class Meta:
        model = User
        fields = ['username', 'password']


