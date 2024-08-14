from django.shortcuts import render
from .models import New_about


def index(request):
    projects = New_about.objects.all()
    return render(request, 'new_about/index.html', {'projects': projects})


