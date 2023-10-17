from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('', views.MusicReviews_home, name='MusicReviews_home'),
    path('AddMusic/', views.MusicReviews_AddMusic, name='MusicReviews_Add_Music'),
    path('MusicReviews/', views.MusicReviews_reviews, name='MusicReviews_reviews'),
    path('<int:pk>/Details/', views.MusicReviews_details, name='music_details'),
    path('<int:pk>/Delete/', views.music_delete, name='music_delete'),
    path('<int:pk>/Update/', views.music_update, name='music_update'),
]
