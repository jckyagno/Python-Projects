from django.urls import path
from . import views

urlpatterns = [
    path('home', views.holidayplanner_home, name='HolidayPlanner_home'),
    path('create/', views.holidayplanner_create, name='HolidayPlanner_create'),
    path('list/', views.holidayplanner_list, name='HolidayPlanner_list'),
    path('<int:pk>/details/', views.holidayplanner_details, name='HolidayPlanner_details'),
    path('<int:pk>/update/', views.holidayplanner_update, name='HolidayPlanner_update'),
    path('<int:pk>/delete/', views.holidayplanner_delete, name='HolidayPlanner_delete'),
    path('api/', views.holidayplanner_api, name='HolidayPlanner_api'),
    path('bs/', views.holidayplanner_bs, name='HolidayPlanner_bs'),
    ]