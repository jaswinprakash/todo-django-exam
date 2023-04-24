from django.shortcuts import render

from users.forms import ToDoTask
from tasks.models import ToDo


def index(request):
    if request.user.is_authenticated:
        instances = ToDo.objects.filter(is_deleted=False)
        form = ToDoTask()
        context = {
            "form": form,
            "title": "ToDo",
            "instances": instances
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