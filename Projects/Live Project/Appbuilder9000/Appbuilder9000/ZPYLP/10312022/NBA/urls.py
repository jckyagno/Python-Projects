from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.NBA_home, name='NBA_home'),
    path('create/', views.createPlayer, name='NBA_create'),
    path('read/', views.nbaRead, name='NBA_read'),
    path('<int:id>/details/', views.nbaDetails, name='nbaDetails'),
]