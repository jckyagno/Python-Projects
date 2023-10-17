from django.urls import path
from . import views


urlpatterns = [
    path('', views.sportstats_home, name='sportstats_home'),
    path('create/', views.sportstats_create, name='sportstats_create'),
    path('display/', views.sportstats_displayall, name='sportstats_displayall'),
    path('<int:pk>/details/', views.sportstats_details, name='sportstats_details'),
    path('<int:pk>/edit/', views.sportstats_edit, name='sportstats_edit'),
    path('<int:pk>/delete/', views.sportstats_delete, name='sportstats_delete'),
    path('soup/', views.sportstats_soup, name='sportstats_soup'),
]
