from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *

# Create your views here.

def loginUsr(request):
    form = loginForm()
    userData = None
    if(request.method == "POST"):
        form = loginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if(user is not None):
                login(request, user)
                userData = UserData.objects.filter(user=user)
                if(len(userData) > 0):
                    response = {'form': form, 'userData': userData[0]}
                    return render(request, 'login.html', response)
                else:
                    response = {'form': form}
                    return render(request, 'login.html', response)
            else:
                messages = ['Incorrect username or password']
                response = {'form': form, 'messages': messages}
                return render(request, 'login.html', response)
    else:
        user = request.user
        if(user.is_authenticated):
            userData = UserData.objects.filter(user=user)
            if(len(userData) > 0):
                response = {'form': form, 'userData': userData[0]}
                return render(request, 'login.html', response)
            else:
                response = {'form': form}
                return render(request, 'login.html', response)
        else:
            response = {'form': form}
            return render(request, 'login.html', response)


def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/authenticate/login/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logoutFunc(request):
    logout(request)
    return redirect('/authenticate/login/')
