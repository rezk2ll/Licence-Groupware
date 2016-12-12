from django.shortcuts import render, HttpResponseRedirect , HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from os import remove
from django.utils.encoding import smart_str
# Create your views here.

from files.models import Filemodel
from files.forms import FileForm
from groupware.settings import UPLOAD_DIR

def NewFile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fform = FileForm(request.POST , request.FILES)
            if fform.is_valid():
                ff = fform.save(commit=False)
                ff.owner = request.user
                ff.name  = request.FILES['filedata'].name
                ff.size  = request.FILES['filedata'].size
                with open(UPLOAD_DIR+ff.name.encode("hex") , "wb+") as f:
                    for chunk in request.FILES['filedata'].chunks():
                        f.write(chunk)
                ff.save()
                return HttpResponseRedirect('/files')
            else:
                return render(request , 'new_file.html' , {'form' : fform})
        else:
            fform = FileForm()
            return render(request , 'new_file.html' , {'form':fform})
    return HttpResponseRedirect('/files')

@login_required(login_url='/login')
def ViewFiles(request):
    filelist = Filemodel.objects.all()
    for fi in filelist:
        fi.size /= 1024
    return render(request , 'files.html' , {'files' : filelist[::-1] , 'nfiles' : len(filelist)})

@login_required(login_url='/login')
def DeleteFile(request , fileid):
    if request.user.is_staff:
        try:
            ff = Filemodel.objects.get(id=fileid)
            fname = UPLOAD_DIR+ff.name.encode("hex")
            ff.delete()
            remove(fname)
        except ObjectDoesNotExist:
            pass
        except WindowsError:
            pass
    return HttpResponseRedirect('/files')

@login_required(login_url='/login')
def DownloadFile(request , fileid):
    try:
        ff = Filemodel.objects.get(id=fileid)
        wrapper = open(UPLOAD_DIR+ff.name.encode("hex") , 'rb')
        response = HttpResponse(wrapper.read())
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(ff.name)
        response['Content-Length'] = ff.size
        return response
        ff.close()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect('/files')
