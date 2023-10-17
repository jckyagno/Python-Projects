from django.urls import path
from . import views

urlpatterns = [
    path('', views.Sneakers_home, name="Sneakers_home"),
    path('create/', views.create_sneaker, name='create'),
    path('current/', views.current_sneakers,name='current'),
    path('sneakDetails/<shoe_id>/', views.sneakersDetails, name='Details'),
]