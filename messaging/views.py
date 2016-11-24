from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from messaging.forms import MessageForm
from messaging.models import Mail
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

@login_required(login_url='/login')
def send_mail(request):
    if request.method == "POST":
        merrors = False
        additiveerror = ""
        mailform = MessageForm(request.POST)
        u  = User.objects.get_by_natural_key(username=request.user.username)
        if mailform.is_valid():
            try:
                u2 = User.objects.get_by_natural_key(username=mailform.cleaned_data["reciver"])
                if not u2 == None:
                    if u.username != u2.username:
                        umail = Mail.objects.create(sender=request.user.username ,reciver=mailform.cleaned_data["reciver"] ,subject=mailform.cleaned_data['subject'] , message=mailform.cleaned_data['message'])
                        umail.save()
                    else:
                        merrors = True
                        additiveerror = "you cannot send mails to yourself"
            except ObjectDoesNotExist:
                merrors = True
                additiveerror = "destination user cannot be found"
        else:
            merrors = True
        return render(request , "mail.html" , {'form' : mailform , 'merrors' : merrors , 'additiveerror' : additiveerror})
    else:
        uform = MessageForm()
        return render(request ,'mail.html' , {'form' :uform })

def inbox(request):
    mails = Mail.objects.filter(reciver=request.user)
    return render(request , 'inbox.html' , {'mails' : mails})

def readmail(request , mailid):
    try:
        reqmail = Mail.objects.get(id=mailid)
        if reqmail == None or reqmail.reciver != request.user:
            return render(request , 'view_mail.html' , {'mail' : reqmail })
    except ObjectDoesNotExist:
        pass
    return render(request , 'home.html' , {'mailsn' : Mail.objects.filter(reciver=request.user).__len__() })


def deletemail(request , mailid):
    try:
        reqmail = Mail.objects.get(id=mailid)
        if reqmail == None or reqmail.reciver != request.user:
            reqmail.delete()
            return HttpResponseRedirect('/mail')
    except ObjectDoesNotExist:
        pass
    return render(request , 'home.html' , {'mailsn' : Mail.objects.filter(reciver=request.user).__len__() })
