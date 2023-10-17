from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.mtb_dest_home, name='mtb_dest_home'),
    path('add/', views.mtb_dest_add, name='mtb_dest_add'),
    path('list/', views.mtb_dest_list, name='mtb_dest_list'),
    path('<int:id>/', views.mtb_dest_details, name='mtb_dest_details'),
    path('<int:id>/edit/', views.mtb_dest_edit, name='mtb_dest_edit'),
    path('<int:id>/delete/', views.mtb_dest_delete, name='mtb_dest_delete'),
    path('confirm_delete/', views.mtb_dest_confirm_delete, name='mtb_dest_confirm_delete'),
    path('api/', views.mtb_dest_api, name='mtb_dest_api'),
    path('bs/', views.mtb_dest_bs, name='mtb_dest_bs'),
]


urlpatterns += staticfiles_urlpatterns()
