from django.shortcuts import render
from tasks.forms import taskForm
from tasks.models import task
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
# Create your views here.
def CreateTask(request):
    if request.method == "POST":
        taskf = taskForm(request.POST)
        if request.user.is_staff:
            if taskf.is_valid():
                t = task.objects.create(subject=taskf.cleaned_data['subject'] , priority=taskf.cleaned_data['priority'] , progress=taskf.cleaned_data['progress'] , content=taskf.cleaned_data['content'])
                t.save()
                return HttpResponseRedirect('/tasks')
            else:
                return render(request,'new_task.html',{'errors':True,'form':taskf , 'action' : '/tasks/new' , 'do':'Create'})
        return HttpResponseRedirect('/tasks')
    else:
        taskf = taskForm()
        return render(request , 'new_task.html', {'form' : taskf , 'action':'/tasks/new' , 'do':'Create'})

def ViewTasks(request):
    tasklist = task.objects.all()
    return render(request , 'tasks.html' , {'tasklist':tasklist[::-1], 'ntasks':tasklist.__len__()})


def DeleteTask(request , taskid):
    try:
        if request.user.is_staff:
            task.objects.get(id=taskid).delete()
            return HttpResponseRedirect('/tasks')
        else:
            return HttpResponseRedirect('/tasks')
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/tasks')


def EditTask(request , taskid):
    if request.method == "GET":
        try:
            if request.user.is_staff:
                t = task.objects.get(id=taskid)
                tform = taskForm(initial={'subject': t.subject , 'priority' : t.priority , 'content' : t.content , 'progress':t.progress})
                return render(request ,'new_task.html' , {'action':'/tasks/edit/%s' % taskid , 'form':tform , 'do':'Edit'})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/tasks')
    else:
        if request.user.is_staff:
            try:
                tform = taskForm(request.POST)
                if tform.is_valid():
                    t = task.objects.get(id=taskid)
                    t.subject   = tform.cleaned_data["subject"]
                    t.progress  = tform.cleaned_data["progress"]
                    t.content   = tform.cleaned_data["progress"]
                    t.priority  = tform.cleaned_data["priority"]
                    t.save()
                    return HttpResponseRedirect("/tasks")
                else:
                    return render(request,'new_task.html',{'errors':True,'form':tform , 'action' : '/tasks/edit/%s' % taskid , 'do':'Edit'})
            except ObjectDoesNotExist:
                pass
        return HttpResponseRedirect("/")
