from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.ja3_home, name='ja3_home'),
    path('enroll/', views.ja3_enroll, name='ja3_enroll'),
    path('<int:pk>/details/', views.details, name='ja3_details'),
    path('<int:pk>/delete/', views.delete, name='ja3_delete'),
    path('confirmdelete/', views.confirmed, name='ja3_confirmed'),
    path('createrecord/', views.createRecord, name='ja3_createRecord'),
    path('roster/', views.roster, name='ja3_roster'),
    path('api/', views.api, name='ja3_api'),
]