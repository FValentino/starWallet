from django.shortcuts import render

def record(request):
    template_name = 'users/record.html'

    return render(request, template_name, {})