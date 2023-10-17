
from django.urls import path
from . import views

urlpatterns = [
    path('', views.onlineartists_home, name='onlineartists_home'),
    path('add/', views.onlineartists_create, name='onlineartists_add'),
    path('all/', views.onlineartists_all, name='onlineartists_all'),
    path('<int:pk>/details/', views.onlineartists_details, name='onlineartists_details'),
    path('<int:pk>/edit/', views.onlineartists_edit, name='onlineartists_edit'),
    path('<int:pk>/delete/', views.onlineartists_delete, name='onlineartists_delete'),
    path('api/', views.onlineartists_api, name='onlineartists_api'),

]