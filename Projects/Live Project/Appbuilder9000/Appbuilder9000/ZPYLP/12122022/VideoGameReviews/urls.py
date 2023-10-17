from django.urls import path
from . import views
from . import models

urlpatterns = [
    path('', views.video_game_home, name='video_game_home'),
    path('create', views.video_game_create, name='video_game_create'),
    path('display', views.video_game_display, name='video_game_display'),
    # .as_view() required to make search work
    path('search', views.SearchResults.as_view(), name='video_game_search'),
    path('details/<int:pk>', views.video_game_details, name='video_game_details'),
    path('edit/<int:pk>', views.video_game_edit, name='video_game_edit'),
    path('delete/<int:pk>', views.video_game_delete, name='video_game_delete'),
    path('api', views.video_game_api, name='video_game_api'),
    path('beautiful_soup', views.video_game_beautiful_soup, name='video_game_beautiful_soup'),
]
