from django.urls import path
from users import views

app_name = "users"


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create_task/', views.create_task, name='create_task'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('finish_task/<int:id>/', views.finish_task, name='finish_task'),
    path('revise_task/<int:id>/', views.revise_task, name='revise_task'),
]
