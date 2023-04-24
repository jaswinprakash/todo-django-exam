from django.urls import path
from users import views

app_name = "users"


urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('users/create_task', views.create_task, name='create_task'),
]
