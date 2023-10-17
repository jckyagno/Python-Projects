from django.urls import path
from .import views

urlpatterns = [
    path('', views.travel_home, name='Travel_home'),
    path('create/', views.travel_create, name='Travel_create'),
    path('read/', views.travel_read, name='Travel_read'),
    path('<int:pk>/details/', views.travel_details, name='Travel_details'),
    path('<int:pk>/update/', views.travel_edit, name='Travel_edit'),
    path('<int:pk>/delete/', views.travel_delete, name='Travel_delete'),
    path('api/', views.travel_api, name='Travel_API'),
    path('bs/', views.travel_bs, name='Travel_BS'),
    path('<int:m>/save_api/', views.travel_save_api, name='Travel_save_api'),
]
