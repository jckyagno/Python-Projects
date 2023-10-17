from django.urls import path
from . import views

urlpatterns = [
    path('', views.sitcoms_home, name='sitcoms_home'),
    path('create/', views.sitcom_create, name='sitcoms_create'),
    path('read/', views.sitcom_read, name='sitcoms_read'),
    path('<int:pk>/details/', views.sitcom_details, name='sitcoms_details'),
    path('<int:pk>/update/', views.sitcom_update, name='sitcoms_update'),
    path('<int:pk>/delete/', views.sitcom_delete, name='sitcoms_delete'),
    path('api/', views.sitcom_api, name='sitcoms_api'),
    path('<int:m>/save_api/', views.sitcom_save_api, name='sitcoms_save_api'),
]
