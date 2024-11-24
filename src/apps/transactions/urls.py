from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns=[
    path('deposito/', views.create_deposit, name='deposito'),
]