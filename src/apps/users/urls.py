from django.urls import path
from django.contrib.auth import views as views_django
from .views.auth_view import login, register

app_name = 'users'

urlpatterns=[
    path('login/', login, name='login'),
    path('register/', register, name="register"),
    path('logout/', views_django.logout_then_login, name='logout')
]