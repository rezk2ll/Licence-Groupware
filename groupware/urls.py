"""groupware URL Configuration

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
from django.conf.urls import url , include
from django.contrib import admin
from groupware.views import *
from accounts.views import register , change_avatar
from messaging.views import send_mail , inbox , readmail , deletemail
from django.contrib.auth.views import login , logout , password_change , password_change_done
from tasks.views import CreateTask , ViewTasks  ,DeleteTask , EditTask
from projects.views import CreateProject , ViewProjects , DeleteProject
from blog.views import viewPosts , NewPost , DeletePost , viewPost , postComment , DeleteComment , EditPost
from files.views import ViewFiles , NewFile , DownloadFile , DeleteFile
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , IndexPage),
    url(r'^login$',login),
    url(r'^logout$',logout),
    url(r'^register$',register),
    url(r'^change-password$',password_change,name="password-change"),
    url(r'^change-password-done$',password_change_done,name="password_change_done"),
    url(r'^change-avatar$',change_avatar),
    url(r'^mail$',inbox),
    url(r'^mail/send$',send_mail),
    url(r'^mail/inbox/(\d+)$',readmail),
    url(r'^mail/delete/(\d+)$',deletemail),
    url(r'^projects/(\d+)/tasks/new$',CreateTask),
    url(r'^tasks$',ViewTasks),
    url(r'^projects/(\d+)/tasks/delete/(\d+)$',DeleteTask),
    url(r'^projects/(\d+)/tasks/edit/(\d+)$',EditTask),
    url(r'^projects/new$',CreateProject),
    url(r'^projects$',ViewProjects),
    url(r'^projects/(\d+)/delete$',DeleteProject),
    url(r'^projects/(\d+)/tasks$',ViewTasks),
    url(r'^blog$',viewPosts),
    url(r'^blog/new$',NewPost),
    url(r'^blog/delete/(\d+)$',DeletePost),
    url(r'^blog/(\d+)$',viewPost),
    url(r'^blog/(\d+)/comment$' , postComment),
    url(r'^blog/(\d+)/comment/(\d+)/delete$',DeleteComment),
    url(r'^blog/edit/(\d+)$',EditPost),
    url(r'^files$',ViewFiles),
    url(r'^files/new$',NewFile),
    url(r'^files/download/(\d+)$',DownloadFile),
    url(r'^files/delete/(\d+)$',DeleteFile),
]
