from django.shortcuts import render

def view_profile(request):
    template_name = 'profile/profile.html'

    return render(request, template_name, {})


def update_profile(request):
    template_name = 'profile/update.html'

    return render(request, template_name, {})
