from django.urls import path

from . import views

urlpatterns = [

    path('', views.carcollection_home, name='carcollection_home'),
    path('create/', views.vehicle_create, name='vehicle_create'),
    path('inventory/', views.CarCollection_inventory, name='carcollection_inventory'),
    path('<int:pk>/details/', views.CarCollection_details, name='carcollection_details'),
    # path('<int:pk>/update/', views.vehicle_update, name='vehicle_update'),
    # path('<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
]