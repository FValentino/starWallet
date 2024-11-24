from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='home'),
    path('usuarios/', include("apps.users.urls")),
    path('transacciones/', include('apps.transactions.urls'))
]
