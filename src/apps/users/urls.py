from django.urls import path
from django.contrib.auth import views as views_django
from .views import auth_view, profile_view, transaction_view

from django.conf import settings
from django.conf.urls.static import static

app_name = 'users'

urlpatterns=[
    #USER
    path('login/', auth_view.login, name='login'),
    path('register/', auth_view.register, name="register"),
    path('logout/', views_django.logout_then_login, name='logout'),
    path('all-users/', auth_view.user_list, name='user_list'),
    path('desactivate/<int:user_id>/', auth_view.desactivate_user, name='desactivate_user'),

    #PROFILE
    path('perfil/', profile_view.view_profile, name='profile'),
    path('perfil/editar', profile_view.update_profile, name='update'),
    path('edit_user/<int:user_id>/', profile_view.edit_user, name='edit_user'),

    #TRANSACTIONS
    path('perfil/historial', transaction_view.transaction_history, name='historial'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)