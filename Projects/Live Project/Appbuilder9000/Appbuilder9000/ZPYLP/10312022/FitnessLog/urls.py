from django.urls import path
from . import views

urlpatterns = [
    path('', views.fitness_home, name='fitness_home'),
    path('entry_create/', views.create_entry, name='fitness_entry_create'),
    path('read/', views.fitness_read, name='fitness_read'),
    path('<int:pk>/details/', views.fitness_details,  name='fitness_details'),
    path('<int:pk>/delete/', views.fitness_delete,  name='fitness_delete'),
    path('<int:pk>/update/', views.fitness_update,  name='fitness_update'),
]




