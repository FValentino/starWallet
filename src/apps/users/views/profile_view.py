from django.http import Http404
from django.shortcuts import redirect, render
from ..forms import UpdateUser

from ..models import CustomUser

def view_profile(request):
    template_name = 'profile/profile.html'

    return render(request, template_name, {})


def update_profile(request):
    template_name = 'profile/update_profile.html'
    
    user = request.user

    form = UpdateUser(instance=user)

    if request.method == 'POST':
        form = UpdateUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')

    return render(request, template_name, {'form': form})


def edit_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        raise Http404("El usuario no existe.")
    
    form = UpdateUser(instance=user)
    template_name = 'profile/update_profile.html'

    if request.method == 'POST':
        form = UpdateUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            
            return redirect('users:user_list')

    return render(request, template_name, {'form': form, 'user': user})