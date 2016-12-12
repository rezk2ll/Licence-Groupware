from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from accounts.models import UserProfile
from accounts.forms import UserCreationForm , UserProfileForm
from groupware.settings import AVATAR_DIR
from shutil import copyfile
def register(request):
    if request.method == "POST":
        uform = UserCreationForm(request.POST)
        if uform.is_valid():
            User.objects.create_user(username=uform.cleaned_data['username'] , password=uform.cleaned_data['password1'] , email=uform.cleaned_data['email'])
            prof = UserProfile(user=User.objects.get(username=uform.cleaned_data['username']))
            prof.save()
            copyfile(AVATAR_DIR+"user.png" , AVATAR_DIR+uform.cleaned_data['username'])
            return render(request , 'registration/success.html')
        else:
            return render(request , 'registration/register.html' , {'errors' : True , 'form' : uform})
    else:
        form = UserCreationForm()
        return render(request , 'registration/register.html' , {'form' : form})


def change_avatar(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            profileform = UserProfileForm(request.POST , request.FILES)
            if profileform.is_valid():
                pf        = profileform.save(commit=False)
                pf.user   = request.user
                pf.link   = request.FILES['avatar'].name
                if pf.link[-3:] not in ['png' , 'jpg' , 'gif']:
                    pass
                else:
                    with open(AVATAR_DIR+pf.user.username , "wb+") as f:
                        print AVATAR_DIR+pf.user.username
                        for chunk in request.FILES['avatar'].chunks():
                            f.write(chunk)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'update_avatar.html' , {'form' : profileform , 'merrors' : True })
        else:
            pform = UserProfileForm()
            return render(request , 'update_avatar.html' , {'form' : pform })
    else:
        return HttpResponseRedirect("/")
