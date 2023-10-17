from django.urls import path
from . import views

urlpatterns = [
    path('', views.dirtbikes_home, name='dirtbikes_home'),
    path('create/', views.dirtbikes_create, name='dirtbikes_create'),
    path('read/', views.dirtbikes_read, name='dirtbikes_read'),
    path('<int:pk>/details/', views.dirtbikes_details, name='dirtbikes_details'),
    path('<int:pk>/update/', views.dirtbikes_update, name='dirtbikes_update'),
    path('<int:pk>/delete/', views.dirtbikes_delete, name='dirtbikes_delete'),
]
