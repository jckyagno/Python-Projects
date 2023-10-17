from django.urls import path
from . import views

urlpatterns = [
    path('', views.procreate_home, name='procreate_home'),
    path('create/', views.procreate_create, name='procreate_create'),
    path('seeartist/', views.procreate_seeartist, name='procreate_seeartist'),
    path('<int:pk>/localhost/Procreate/1/Procreate_details/', views.procreate_details, name='procreate_details'),
]