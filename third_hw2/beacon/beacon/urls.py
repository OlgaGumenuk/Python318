"""
URL configuration for beacon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from beaco import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),

    # Beacon
    path('current', views.currentbeacon, name='currentbeacon'),
    path('', views.home, name='home'),
    path('create/', views.createbeaco, name='createbeaco'),
    path('beaco/<int:beaco_pk>/', views.viewbeaco, name='viewbeaco'),
    path('beaco/<int:beaco_pk>/complete', views.completebeaco, name='completebeaco'),
    path('completed/', views.completedbeacon, name='completedbeacon'),
    path('beaco/<int:beaco_pk>/delete', views.deletebeaco, name='deletebeaco'),
    #  после <int:beaco_pk> динамическая часть пути
]
