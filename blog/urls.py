"""blog3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from posts import views as posts_views
from users import views as users_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', posts_views.home , name = 'home'),
    url(r'^detail/(?P<id>\d+)', posts_views.detail, name = 'detail'),
    url(r'^create$', posts_views.create , name = 'create'),
    url(r'^update/(?P<id>\d+)', posts_views.update, name = 'update'),
    url(r'^delete/(?P<id>\d+)$', posts_views.delete , name ='delete'),
    url(r'^register/$', users_views.register , name ='register'),
    url(r'^login/$', users_views.login , name ='login'),
    url(r'^logout/$', users_views.logout , name ='logout'),
    url(r'^about/$', posts_views.about , name ='about'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)