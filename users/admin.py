from django.contrib import admin

from tasks.models import ToDo, Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name","user"]

admin.site.register(Author,AuthorAdmin)


class AdminToDo(admin.ModelAdmin):
    list_display = ["id", "add_task"]

admin.site.register(ToDo,AdminToDo)