from dataclasses import field
from django import forms
from django.contrib.auth.models import User

class RegisterationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email']

    # we can use clear_ function for check attr in form
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("passwords don't match!!")
        return cd['password2']

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)