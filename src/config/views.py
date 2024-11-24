from django.shortcuts import render

def inicio(request):
    template_name = 'home.html'

    return render(request, template_name, {})