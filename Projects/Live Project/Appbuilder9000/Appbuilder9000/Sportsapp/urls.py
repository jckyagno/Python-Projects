from django.urls import path
from . import views

urlpatterns = [
    path('', views.Sports_home, name='Sports_home'),
    path('scores', views.Sports_scores, name='Sports_scores'),
    path('<int:pk>/scores', views.Sports_scores, name='Sports_scores'),
    # path('update/', views.Sports_update, name='Sports_update'),
    path('create', views.Sports_create, name='Sports_create'),
    path('<int:pk>/details/', views.Sports_details, name='Sports_details'),
    path('<int:pk>/update/', views.Sports_update, name='Sports_update'),
    path('<int:pk>/delete/', views.Sports_delete, name='Sports_delete'),
    path('<int:pk>/edit/', views.Sports_edit, name='Sports_edit'),
    path('api', views.Sports_api, name='Sports_api'),

]


