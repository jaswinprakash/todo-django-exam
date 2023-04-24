from django.shortcuts import render

from users.forms import ToDoTask


def index(request):
    form = ToDoTask
    context = {
        "form": form,
        "title": "ToDo"
    }
    return render(request, 'index.html',context=context)