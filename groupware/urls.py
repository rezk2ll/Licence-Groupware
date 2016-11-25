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
from accounts.views import register
from messaging.views import send_mail , inbox , readmail , deletemail
from django.contrib.auth.views import login , logout
from tasks.views import CreateTask , ViewTasks  ,DeleteTask , EditTask
from projects.views import CreateProject , ViewProjects , DeleteProject
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$' , IndexPage),
    url(r'^login$',login),
    url(r'^logout$',logout),
    url(r'^register$',register),
    url(r'^mail$',inbox),
    url(r'^mail/send$',send_mail),
    url(r'^mail/inbox/(\d+)$',readmail),
    url(r'^mail/delete/(\d+)$',deletemail),
    url(r'^projects/(\d+)/tasks/new$',CreateTask),
    url(r'^tasks$',ViewTasks),
    url(r'^tasks/delete/(\d+)$',DeleteTask),
    url(r'^projects/(\d+)/tasks/edit/(\d+)$',EditTask),
    url(r'^projects/new$',CreateProject),
    url(r'^projects$',ViewProjects),
    url(r'^projects/(\d+)/delete$',DeleteProject),
    url(r'^projects/(\d+)/tasks$',ViewTasks),

]
