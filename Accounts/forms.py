from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class PermissionSelectForm(forms.Form):

    def __init__(self, queryset, nm, *args, **kwargs):
        super(PermissionSelectForm, self).__init__(*args, **kwargs)
        self.fields[f"{nm}"] = forms.ModelMultipleChoiceField(queryset=queryset, widget=forms.SelectMultiple(
            {'class': 'form-control', 'style': "height: 267.594px; width:150;", 'id': f"id_{nm}"}))


class CustomUserCreationForm(UserCreationForm):
    model = User
    fields = ['username', 'password1', 'password2', 'user_permissions', ]
