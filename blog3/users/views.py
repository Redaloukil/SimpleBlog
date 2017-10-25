# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render ,redirect
from django.contrib import auth 
from django.contrib.auth.models import User
from django.contrib import messages
# from posts.views import home
# Create your views here.

def login(request):
    if request.method == "POST" :
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request , username = username , password = password)
        if user is not None :
            auth.login(request, user)
            messages.success(request ,"welcome{}".format(user.username))
            return redirect("home")
        else:
            messages.error(request ,"wrong username or password ")
            return render(request,"login.html",{})
    else:
        return render(request,"login.html",)

def logout(request):
    auth.logout(request)
    return redirect("home")

def register(request):
    if request.method == "POST" :
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if User.objects.filter(username = username).exists():
            messages.error(request,"this username exists")
            return render(request , "register.html")
        if User.objects.filter(email = email).exists():
            messages.error(request,"this email exists")
            return render(request , "register.html")
        if password != confirm_password:
            messages.error(request,"this email exists")
            return render(request , "register.html")
        
        user = User.objects.create_user(username , email = email , password=password, is_staff= True , is_superuser = True)
        user = auth.authenticate(request , username= username , password=password)
        messages.success(request , "think you for registration")
        return redirect("home")
    else:
        return render(request,"register.html")
    