from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Nutrition_Home, name = 'Nutrition_Home'),
    path('Nutrition_create/', views.registerform, name = 'Nutrition_create'),
    path('<int:pk>/details/', views.userdetails, name='Nutrition_User_Details'),
    path('<int:pk>/edit/', views.edit, name = 'Nutrition_edit'),
    path('<int:pk>/delete/', views.delete, name = 'Nutrition_delete'),
    path('Nutrition_Display/', views.displayusers, name = 'Nutrition_display'),
    path('confirmdelete', views.confirmDelete, name="confirmDelete"),
    path('api/', views.Nutrition_api, name = "Nutrition_api"),
    path('beautifulSoup/', views.Nutrition_beautifulSoup, name = 'Nutrition_beautifulSoup'),
]