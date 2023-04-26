from django.shortcuts import render
from django.contrib.auth.decorators import login_required



from users.forms import ToDoTask
from tasks.models import ToDo

@login_required(login_url="users/login/")
def index(request):
    if  request.user.is_authenticated:
        username = request.user
        instances = ToDo.objects.filter(is_deleted=False,username=username,is_completed=False)
        completed_instances = ToDo.objects.filter(is_deleted=False,username=username,is_completed=True)
        form = ToDoTask()
        context = {
            "form": form,
            "title": "ToDo",
            "instances": instances,
            "completed_instances": completed_instances
        }
        return render(request, 'index.html',context=context)

    else:
        instances = ToDo.objects.filter(is_deleted=False)
        form = ToDoTask()
        context = {
            "form": form,
            "title": "ToDo",
        }
        return render(request, 'index.html',context=context)
