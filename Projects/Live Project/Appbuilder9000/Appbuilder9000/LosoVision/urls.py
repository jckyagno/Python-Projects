from django.urls import path
from . import views

urlpatterns = [
    path('', views.loso_home, name='LosoVision_home'),
    path('Add_Patient/', views.loso_create, name='LosoVision_create'),
    path('Patient_Info/', views.loso_read, name='LosoVision_read'),
]