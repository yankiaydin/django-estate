from django import forms
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirmation = forms.CharField(label="Password Again", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "confirmation",
            "email",
            "first_name",
            "last_name",
        ]


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        values = {"username": username, "password": password}
        return values
