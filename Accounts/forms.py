from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from .models import *


class EmoployeeForm(forms.ModelForm):
    model = Employee
    fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

# class PermissionForm(forms.ModelForm):
#     model = Permission
#
#     class Meta:
#         widgets = {
#             'name' : forms.ModelMultipleChoiceField(attrs={'class':'form-group'})
#         }

class CustomUserCreationForm(UserCreationForm):

    model = User
    fields = ['username', 'password1', 'password2', 'user_permissions', ]
