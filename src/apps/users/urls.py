from django.urls import path
from django.contrib.auth import views as views_django
from .views.auth_view import login, register
from . views.profile_view import view_profile

from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns=[
    #USER
    path('login/', login, name='login'),
    path('register/', register, name="register"),
    path('logout/', views_django.logout_then_login, name='logout'),

    #PROFILE
    path('perfil/', view_profile, name='profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)