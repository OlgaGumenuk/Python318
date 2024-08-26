from django.shortcuts import render, get_object_or_404
from .models import New_maiking


def new_maiking(request):
    new_maiking = New_maiking.objects.order_by('-date')
    return render(request, 'new_maiking/new_maiking.html', {'new_maiking': new_maiking})

def detail(request, new_make_id):
    new_make = get_object_or_404(New_maiking, pk=new_make_id)
    return render(request, 'new_maiking/details.html', {'new_make': new_make})
