from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import BeacoForm
from .models import Beaco
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def signupuser(request):
    if request.method == "GET":
        return render(request, 'beaco/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currentbeacon')
            except IntegrityError:
                return render(request, 'beaco/signupuser.html',
                              {'form': UserCreationForm(),
                              'error': 'Такое имя пользователя уже существует, введите другое'})
        else:
            return render(request, 'beaco/signupuser.html', {'form': UserCreationForm(),
                                                                 'error': 'Пароли не совпадают'})


@login_required
def currentbeacon(request):
    beacon = Beaco.objects.filter(user=request.user, date_completed__isnull=True)
    # __isnull=True - это доп параметры кот мы можем использовать при фильтрации при поиске каких-то элементов
    return render(request, 'beaco/currentbeacon.html', {'beacon': beacon})

def home(request):
    return render(request, 'beaco/home.html')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def loginuser(request):
    if request.method == "GET":
        return render(request, 'beaco/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'beaco/loginuser.html',
                          {'form': AuthenticationForm(),
                          'error': 'Неверные данные пользователя'})
        else:
            login(request, user)
            return redirect('currentbeacon')


@login_required
def createbeaco(request):
    if request.method == "GET":
        return render(request, 'beaco/createbeaco.html', {'form': BeacoForm()})
    else:
        try:
            form = BeacoForm(request.POST)
            new_beaco = form.save(commit=False)
            new_beaco.user = request.user
            new_beaco.save()
            return redirect('currentbeacon')
        except ValueError:
            return render(request, 'beaco/createbeaco.html',
                          {'form': BeacoForm(),
                           'error': 'Переданы неверные данные. Попробовать бы еще раз.'})


@login_required
def viewbeaco(request, beaco_pk):
    beaco = get_object_or_404(Beaco, pk=beaco_pk)
    if request.method == "GET":
        form = BeacoForm(instance=beaco)  # выведет соот-ую запись из бады данных
        return render(request, 'beaco/viewbeaco.html', {'beaco': beaco, 'form': form})
    else:
        try:
            form = BeacoForm(request.POST, instance=beaco)
            # instance=beaco даст
            # что надо отредактировать существующие данные
            # request.POST собираем указанные данные из быза данных
            form.save()
            return redirect('currentbeacon')
        except ValueError:
            return render(request, 'beaco/viewbeaco.html',
                          {'beaco': beaco, 'form': form,
                           'error': 'Неверные данные'})


@login_required
def completebeaco(request, beaco_pk):
    beaco = get_object_or_404(Beaco, pk=beaco_pk, user=request.user)
    if request.method == "POST":
        beaco.date_completed =timezone.now()
        beaco.save()
        return redirect('currentbeacon')


@login_required
def completedbeacon(request):
    beacon = Beaco.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'beaco/completedbeacon.html', {'beacon': beacon})


@login_required
def deletebeaco(request, beaco_pk):
    beaco = get_object_or_404(Beaco, pk=beaco_pk, user=request.user)
    if request.method == "POST":
        beaco.delete()
        return redirect('currentbeacon')
