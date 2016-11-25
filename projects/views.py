from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from projects.forms import ProjectForm
from projects.models import Project
# Create your views here.
def CreateProject(request):
    if request.method == "POST":
        if request.user.is_staff:
            projform = ProjectForm(request.POST)
            if projform.is_valid():
                p = Project.objects.create(name = projform.cleaned_data['name'] , progress=0)
                p.save()
                return HttpResponseRedirect('/projects')
            else:
                return render(request , 'new_project.html' , {'errors':True , 'form':projform})
        else:
            return HttpResponseRedirect('/projects')
    else:
        projform = ProjectForm()
        return render(request , 'new_project.html' , {'form' : projform})

def ViewProjects(request):
    projectsList = Project.objects.all()
    return render(request , 'projects.html' , {"projects" : projectsList[::-1] , 'nprojects' : projectsList.__len__()})

def DeleteProject(request , projectid):
    try:
        if request.user.is_staff:
            Project.objects.get(id=projectid).delete()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect('/projects')
