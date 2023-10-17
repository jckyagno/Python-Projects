from django.urls import path
from .import views

urlpatterns = [
    path('', views.dyd_home, name='dyd_home'),
]
