from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from accounts.forms import UserCreationForm
def register(request):
    if request.method == "POST":
        uform = UserCreationForm(request.POST)
        if uform.is_valid():
            User.objects.create_user(username=uform.cleaned_data['username'] , password=uform.cleaned_data['password1'] , email=uform.cleaned_data['email'])
            print "done"
            return render(request , 'registration/success.html')
        else:
            return render(request , 'registration/register.html' , {'errors' : True , 'form' : uform})
    else:
        form = UserCreationForm()
        return render(request , 'registration/register.html' , {'form' : form})
