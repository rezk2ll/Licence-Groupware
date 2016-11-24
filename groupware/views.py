from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from messaging.models import Mail
@login_required(login_url='/login')
def IndexPage(request):
    mails = Mail.objects.filter(reciver=request.user).__len__()
    return render(request , 'home.html' , {'mailsn' : mails})
