from django.urls import path
from . import views
from .views import CreateEntry

urlpatterns = [
    path('', views.CustomPcs_home, name='CustomPcs_Home'),
    path('create/', views.CreateEntry, name='BuildForm'),
    path('Entries/', views.Entries, name='AllEntries'),
    path('Details/<int:pk>', views.Details, name='Details'),

]
