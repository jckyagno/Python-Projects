from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

# urls which point to function in views.py

urlpatterns = [
    path('', views.wine_home, name='wine_home'),
    path('Wines/', views.wine_create, name='wine_create'),
    path('Log/', views.wine_log, name='wine_log'),
    path('<int:pk>/details/', views.wine_details, name='wine_details'),
    path('<int:pk>/update/', views.wine_update, name='wine_update'),
    path('<int:pk>/delete/', views.wine_delete, name='wine_delete'),

]
