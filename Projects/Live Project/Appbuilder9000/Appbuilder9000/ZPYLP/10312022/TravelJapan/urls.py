from django.urls import path
from . import views

urlpatterns = [
    path('', views.traveljapan_home, name='traveljapan_home'),
    path('create/', views.traveljapan_create, name='traveljapan_create'),
    path('places/', views.traveljapan_places, name='traveljapan_places'),
    path('<int:pk>/details/', views.traveljapan_details, name='traveljapan_details'),
    path('<int:pk>/update/', views.traveljapan_update, name='traveljapan_update'),
    path('<int:pk>/delete/', views.traveljapan_delete, name='traveljapan_delete'),
    path('api/', views.traveljapan_api, name='traveljapan_api'),
    path('bs/', views.traveljapan_bs, name='traveljapan_bs'),
]