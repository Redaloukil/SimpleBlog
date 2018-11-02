from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import json
from time import time
from django.contrib import messages
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Post
from .forms import PostModelForm

# Create your views here.

def home(request):
    posts = Post.objects.order_by('-updated')  
    context = {
        'posts':posts,
        }
    return render(request,'index.html',context)


def detail(request,id):
    title ="datail post"
    post = Post.objects.get(id=id)
    context = {
        'post':post,
        'title':title,
    }
    return render(request , 'detail.html', context)


def create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.POST.get("image")
        article = Post.objects.create(title = title , content = content)
        article.save()
        messages.success(request,"article has been done", extra_tags='some-tag')
        return redirect("home")
    return render(request,'create.html')


def update(request,id):
    post = get_object_or_404( Post, id = id)
    form = PostModelForm(request.POST or None , request.FILES or None ,instance = post)
    if form.is_valid():
        form_succes = form.save(commit = False)
        form_succes.save()
        return redirect("home")
    
    context = {
        'form':form,
        'title':title,
    }   
    return render(request , 'update.html', context)

def delete(request,id):
    post = get_object_or_404( Post,id = id)
    post.delete()
    
    return redirect("home")

def about(request):
    return render(request,"about.html")