from django.shortcuts import render
from tasks.forms import taskForm
from tasks.models import task
from projects.models import Project
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
# Create your views here.
def CreateTask(request , projectid):
    if request.method == "POST":
        taskf = taskForm(request.POST)
        if request.user.is_staff:
            if taskf.is_valid():
                try:
                    p = Project.objects.get(id=taskf.cleaned_data['projid'])
                    team = ", ".join(taskf.cleaned_data['worker'])
                    t = task.objects.create(workers = team  , project=p.id , subject=taskf.cleaned_data['subject'] , priority=taskf.cleaned_data['priority'] , progress=taskf.cleaned_data['progress'] , content=taskf.cleaned_data['content'])
                    t.save()
                except ObjectDoesNotExist:
                    pass
                return HttpResponseRedirect('/projects/%s/tasks' % projectid)
            else:
                return render(request,'new_task.html',{'errors':True,'form':taskf , 'action' : '/projects/%s/tasks/new' % projectid , 'do':'Create' , 'project_id' : projectid})
        return HttpResponseRedirect('/projects/%s/tasks' % projectid)
    else:
        taskf = taskForm()
        return render(request , 'new_task.html', {'form' : taskf , 'action':'/projects/%s/tasks/new' % projectid , 'do':'Create' , 'project_id' : projectid})

def ViewTasks(request , projectid):
    try:
        pname    = Project.objects.get(id=projectid).name
        tasklist = task.objects.filter(project=projectid)
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/projects")
    return render(request , 'tasks.html' , {'tasklist':tasklist, 'ntasks':tasklist.__len__() , 'pname':pname , 'pid':projectid})

def DeleteTask(request , projectid , taskid):
    try:
        if request.user.is_staff:
            p = Project.objects.get(id=projectid)
            task.objects.get(id=taskid).delete()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect('/projects/%s/tasks' % projectid)


def EditTask(request  , projid , taskid):
    if request.user.is_staff:
        if request.method == "GET":
            try:
                if request.user.is_staff:
                    t = task.objects.get(id=taskid)
                    p = Project.objects.get(id=projid)
                    tform = taskForm(initial={'projid':p.id,'subject': t.subject , 'priority' : t.priority , 'content' : t.content , 'progress':t.progress , 'worker' : t.workers})
                    return render(request ,'new_task.html' , {'action':'/projects/%s/tasks/edit/%s' % (projid , taskid), 'project_id':p.id,'form':tform , 'do':'Edit'})
            except ObjectDoesNotExist:
                return HttpResponseRedirect('/projects/%s/tasks' % projid)
        else:
            try:
                tform = taskForm(request.POST)
                if tform.is_valid():
                    team = ",".join(tform.cleaned_data['worker'])
                    t = task.objects.get(id=taskid)
                    p = Project.objects.get(id=projid)
                    t.subject   = tform.cleaned_data["subject"]
                    t.progress  = tform.cleaned_data["progress"]
                    t.content   = tform.cleaned_data["content"]
                    t.priority  = tform.cleaned_data["priority"]
                    t.workers   = team
                    t.save()
                    return HttpResponseRedirect("/projects/%s/tasks" % projid)
                else:
                    return render(request,'new_task.html',{'project_id':projid, 'errors':True,'form':tform , 'action' : '/projects/%s/tasks/edit/%s' % (projid , taskid) , 'do':'Edit'})
            except ObjectDoesNotExist:
                pass
    return HttpResponseRedirect("/")
