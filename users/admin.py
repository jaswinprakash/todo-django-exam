from django.contrib import admin

from users.models import ToDo


class AdminToDo(admin.ModelAdmin):
    list_display = ["id", "add_task"]

admin.site.register(ToDo,AdminToDo)