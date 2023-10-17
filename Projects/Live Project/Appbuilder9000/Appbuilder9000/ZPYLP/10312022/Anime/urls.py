from django.urls import path
from . import views


urlpatterns = [
    path('', views.anime_home, name='anime_home'),
    path('create/', views.create_anime, name='create_anime'),
    path('anime_archive/', views.anime_archive, name='anime_archive'),
    path('<int:pk>/details/', views.anime_details, name='anime_details'),
    path('<int:pk>/update/', views.anime_update, name='anime_update'),
    path('<int:pk>/delete/', views.anime_delete, name='anime_delete'),
]
