from django.urls import path
from . import views

urlpatterns = [
    path('', views.dfort_home, name='dfort_home'),
    path('create/', views.dfort_create, name='dfort_create'),
    path('display/', views.dfort_display, name='dfort_display'),
    path('search/', views.dfort_search, name='dfort_search'),
    path('<int:pk>/details/', views.dfort_details, name='dfort_details'),
    path('<int:pk>/edit/', views.dfort_edit, name='dfort_edit'),
    path('<int:pk>/delete/', views.dfort_delete, name='dfort_delete'),
    path('news/', views.dfort_news, name='dfort_news'),
    path('about/', views.dfort_about, name='dfort_about'),
    path('api/', views.dfort_api, name='dfort_api'),
    path('<>/save/', views.dfort_save, name='dfort_save'),
    path('list/', views.dfort_list, name='dfort_list'),
    path('arena/', views.dfort_arena, name='dfort_arena'),
    path('results/', views.dfort_results, name='dfort_results'),
    path('error/', views.dfort_error, name='dfort_error'),
]