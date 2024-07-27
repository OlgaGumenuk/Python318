from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    adr = "ДНР, г.Донецк, ул.Мира, 65"
    tel = "7-949-328-34-39"
    return render(request, "bower/home.html", {'title': 'Ваша беседка', 'address': adr,
                                               'telephon': tel})

def stylebower(request):
    return render(request, "bower/stylebower.html")

def registration(request):
    return render(request, "bower/registration.html")