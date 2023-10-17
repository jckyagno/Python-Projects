from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_home, name='inventory_home'),
    path('create/', views.inventory_create, name='inventory_create'),
    path('read/', views.inventory_read, name='inventory_read'),
    path('search/', views.SearchResultsView.as_view(), name='inventory_search'),
    path('<int:pk>/details/', views.inventory_details, name='inventory_details'),
    path('<int:pk>/update/', views.inventory_update, name='inventory_update'),
    path('<int:pk>/delete/', views.inventory_delete, name='inventory_delete'),
]