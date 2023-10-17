from django.urls import path
from . import views

urlpatterns = [
    path('', views.journalbs_home, name='journalbs_home'),
    path('create/', views.journalbs_create, name='journalbs_create'),
    path('read/', views.journalbs_read, name='journalbs_read'),
    path('<int:pk>/details/', views.journalbs_details, name='journalbs_details'),
    path('<int:pk>/update/', views.journalbs_update, name='journalbs_update'),
    path('<int:pk>/delete/', views.journalbs_delete, name='journalbs_delete'),
]
