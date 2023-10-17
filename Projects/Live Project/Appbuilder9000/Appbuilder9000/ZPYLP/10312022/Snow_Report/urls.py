from django.urls import path
from . import views


urlpatterns = [
    path('', views.snow_report_home, name='snow_report_home'),
    path('addResort/', views.snow_report_addResort, name='snow_report_addResort'),
    path('favorites/', views.snow_report_favorites, name='snow_report_favorites'),
    path('<int:pk>/details/', views.snow_report_details, name='snow_report_details'),
    path('<int:pk>/update/', views.snow_report_update, name='snow_report_update'),
    path('<int:pk>/delete/', views.snow_report_delete, name='snow_report_delete'),
    path('api/', views.snow_report_api, name='snow_report_api'),
    path('<int:m>/save_api/', views.snow_report_save_api, name='snow_report_save_api'),
    path('<int:pk>/details_api/', views.snow_report_details_api, name='snow_report_details_api'),
    path('<int:pk>/delete_api/', views.snow_report_delete_api, name='snow_report_delete_api'),
    path('bs/', views.snow_report_bs, name='snow_report_bs'),


]
