from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_maiking, name='new_maiking'),
    path('<int:new_make_id>/', views.detail, name='detail'),
]