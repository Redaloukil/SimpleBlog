# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','updated']
    list_filter = ['title','updated']
    fields = ['title','content','image']
    ordering = ['-updated']
    class Meta:
        model = Post
        
admin.site.register(Post , PostModelAdmin)
