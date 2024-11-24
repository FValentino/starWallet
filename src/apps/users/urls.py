from django.urls import path
from .views.auth_view import login, register

app_name = 'users'

urlpatterns=[
    path('login/', login, name='login'),
    path('new-user/', register, name="register")
]