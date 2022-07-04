from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .forms import RegisterationForm, UserLoginForm

def register_user(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
        
    else:
        form = RegisterationForm()

    return render(request, 'account/register.html', {'form' : form})

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            print('form is valid')
            
    else:
        form = UserLoginForm()

    return render(request, 'account/login.html', {'form_class':form})