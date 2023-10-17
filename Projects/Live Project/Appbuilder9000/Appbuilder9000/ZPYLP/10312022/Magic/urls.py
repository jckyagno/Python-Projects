from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.magic_home, name='magic_home'),
    path('create/', views.magic_create, name='magic_create'),
    path('browse/', views.magic_browse, name='magic_browse'),
    path('<int:pk>/details/', views.magic_details, name='magic_details'),
    path('<int:pk>/edit/', views.magic_edit, name='magic_edit'),
    path('<int:pk>/delete/', views.magic_delete, name='magic_delete'),
    path('<int:pk>/details/delete_c/', views.delete_c, name='delete_c'),
    path('api/', views.magic_api, name='magic_api'),
]