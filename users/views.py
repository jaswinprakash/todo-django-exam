from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from users.forms import UserForm, ToDoTask
from tasks.models import ToDo
from main.functions import generate_form_errors


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request,username=username, password=password)
            if user is not None:
                auth_login(request,user)

                return HttpResponseRedirect("/")
            else:
                context = {
                        "title": "Login",
                        "error": True,
                        "message": "Invalid username or password"
                    }
                return render(request, "users/login.html", context=context)
        else:
                context = {
                        "title": "Login",
                        "error": True,
                        "message": "Invalid username or password"
                    }
                return render(request, "users/login.html", context=context)
    else:
        context = {
            "title" : "Student Login"
        }
        return render(request, "users/login.html", context=context)

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("web:index"))

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            User.objects.create_user(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name,
            )

            user = authenticate(request, username=instance.username, password=instance.password)
            auth_login(request,user)

            return HttpResponseRedirect(reverse("web:index"))
        else:
            message = generate_form_errors(form)

            form = UserForm()
            context = {
                    "title": "Sign Up",
                    "error": True,
                    "message": message,
                    "form": form,
                }
            return render(request, "users/signup.html", context=context)
    else:
        form = UserForm()
        context = {
            "title" : "Sign Up",
            "form" : form,
        }
        return render(request, "users/signup.html", context=context)
    

@login_required
def create_task(request):
    if request.method == "POST":
        form = ToDoTask(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()

            return HttpResponseRedirect(reverse('web:index'))
    else:
         form = ToDoTask()
         instances = ToDo.objects.filter(is_deleted=False)    
         context = {
                "title" : "Home Page",
                "instances": instances,
                "message" : generate_form_errors(form),
                "form":form
            }
         return render(request, 'web:index', context=context)


@login_required
def edit_task(request):
    pass


@login_required
def delete_task(request):
    pass


@login_required
def finish_task(request):
    pass