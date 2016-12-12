from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from messaging.models import Mail
from blog.models import Post , Comment
from projects.models import Project
from tasks.models import task
from files.models import Filemodel
from django.contrib.auth.models import User

@login_required(login_url='/login')
def IndexPage(request):
    mails = Mail.objects.filter(reciver=request.user).__len__()
    users = User.objects.all().__len__()
    tasks = task.objects.all().__len__()
    projs = Project.objects.all().__len__()
    posts = Post.objects.all().__len__()
    files = Filemodel.objects.all().__len__()
    comms = Comment.objects.all().__len__()
    request.mailsn = mails
    return render(request , 'home.html' , {'mailsn' : mails  , 'users':users , 'tasks':tasks , 'projects' : projs , 'posts' : posts , 'files' : files , 'comms':comms})
