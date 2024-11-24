from django.shortcuts import render

def profile(request):
    template_name = 'users/profile.html'

    return render(request, template_name, {})


def favorites(request):
    template_name = 'users/favorites.html'

    return render(request, template_name, {})
