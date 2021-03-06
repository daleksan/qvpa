# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import LoginForm


def loginView(request):
    error_message = None
    currentUrl = request.get_full_path()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('projects/')
                else:
                    print("Аккаунт был отключен!")
            else:
                error_message = "Пользователя с таким логином и паролем не существует!"
    elif request.user.is_authenticated:
        return HttpResponseRedirect('projects/')
    else:
        form = LoginForm()
    return render(request, 'index.html', locals())


def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
