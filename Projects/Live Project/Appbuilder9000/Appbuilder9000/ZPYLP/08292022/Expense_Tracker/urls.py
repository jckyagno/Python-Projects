from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.ET_Home, name='ET_Home'),
    path('add', views.ProjectCreativeView.as_view(), name='add'),
    path('<slug:project_slug>', views.project_detail, name='detail'),
]
