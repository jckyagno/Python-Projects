from django.urls import path
from . import views

urlpatterns = [
    path('', views.SLCRestaurantGuide_home, name='SLCRestaurantGuide_home'),
    path('SLCRestaurantGuide_create/', views.SLCRestaurantGuide_create, name='SLCRestaurantGuide_create'),
    path('SLCRestaurantGuide_view/', views.SLCRestaurantGuide_view, name='SLCRestaurantGuide_view'),
    path('<int:pk>/SLCRestaurantGuide_details/', views.SLCRestaurantGuide_details, name='SLCRestaurantGuide_details'),
    path('<int:pk>/update/', views.SLCRestaurantGuide_update, name='SLCRestaurantGuide_update'),
    path('<int:pk>/delete/', views.SLCRestaurantGuide_delete, name='SLCRestaurantGuide_delete'),
    path('api/', views.SLCRestaurantGuide_api, name='SLCRestaurantGuide_api'),
]

