from django.urls import path
from . import views

urlpatterns = [
    path('', views.bgt_home, name='bgt_home'),
    path('bgt_create/', views.bgt_create, name="bgt_create"),
    path('bgt_view/', views.bgt_view, name="bgt_view"),
    path('<int:pk>/details', views.bgt_details, name='bgt_details'),
    path('<int:pk>/edit/', views.bgt_edit, name='bgt_edit'),
    path('<int:pk>/delete', views.bgt_delete, name='bgt_delete'),
    path('bgt_bsoup_render', views.bgt_bsoup_render, name='bgt_bsoup_render'),
    path('bgt_api', views.bgt_api, name='bgt_api'),

]


