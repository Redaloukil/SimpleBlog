# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL , default = 1)
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(blank=True,null = True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
    
    
    def __str__(self):
        return self.title