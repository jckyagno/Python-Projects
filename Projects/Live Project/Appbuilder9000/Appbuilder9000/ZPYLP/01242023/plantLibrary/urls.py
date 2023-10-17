from django.urls import path
from . import views

urlpatterns = [
    path('', views.plant_home, name='plant_home'),
    path('plant_addplant', views.plant_addplant, name='plant_addplant'),
    path('plant_myplantlibrary', views.plant_myplantlibrary, name='plant_myplantlibrary'),
    path('<int:pk>/plant_details', views.plant_details, name='plant_details'),

    ]
