from django.urls import path
from . import views

urlpatterns = [
    path('', views.datebook_home, name='datebook_home'),
    path('entry/', views.datebook_entry, name='datebook_entry'),
    path('all/', views.datebook_all, name='datebook_all'),
    path('<int:pk>/details/', views.datebook_details, name='datebook_details'),
    path('<int:pk>/update/', views.datebook_update, name='datebook_update'),
    path('<int:pk>/delete/', views.datebook_delete, name='datebook_delete'),
]