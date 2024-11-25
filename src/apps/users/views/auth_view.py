from pyexpat.errors import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login as login_django, authenticate

from ..forms import FormUser
from ..models import CustomUser

def register(request):
    template_name = './users/register.html'

    form = FormUser()
    message = ''

    if request.method == 'POST':
        form = FormUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            message = "No se pudo guardar de forma correcta el formulario"
            print (message)

    ctx = {
        "formUsuario": form,
        "message": message
    }

    return render(request, template_name, ctx)

def login(request):
    template_name = 'users/login.html'

    salio_mal = False
    se_autentico = False
    username = ""

    if request.method == "POST":
        username = request.POST.get("username", default=None)
        password = request.POST.get("password", default=None)
        usuario = authenticate(request, username=username, password=password)
        se_autentico = True
        if usuario:
            salio_mal = False
            login_django(request, usuario)
            return redirect('home')
        else:
            print ('no funciona')

    ctx = {
        "se_autentico": se_autentico,
        "salio_mal": salio_mal,
        "username": username
    }
    return render(request, template_name, ctx)

def user_list(request):
    template_name='users/user_list.html'

    users = CustomUser.objects.all()

    return render(request, template_name, {'users':users})

def desactivate_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        raise Http404("El usuario no existe.")
    
    if user.is_active:
        user.is_active = False
        user.save()

    return redirect('users:user_list')