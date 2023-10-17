from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.fe_Home, name='fe_Home'),
    path('fe_Evaluation', views.fe_Evaluation, name='fe_Evaluation'),
    path('fe_Account', views.fe_Account, name='fe_Account'),
    path('fe_Approach', views.fe_Approach, name='fe_Approach'),
    path('<int:pk>/fe_Delete', views.fe_Delete, name='fe_Delete'),
    path('<int:pk>/fe_Details', views.fe_Details, name='fe_Details'),
    path('fe_Read', views.fe_Read, name='fe_Read'),
    path('<int:pk>/fe_Update', views.fe_Update, name='fe_Update'),
]
