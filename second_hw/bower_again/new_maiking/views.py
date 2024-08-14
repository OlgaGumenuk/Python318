from django.shortcuts import render
from .models import New_maiking


def new_maiking(request):
    new_maiking = New_maiking.objects.order_by('-date')
    return render(request, 'new_maiking/new_maiking.html', {'new_maiking': new_maiking })