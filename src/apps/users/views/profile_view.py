from django.shortcuts import redirect, render
from ..forms import UpdateUser

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
