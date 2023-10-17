from django.urls import path
from . import views

urlpatterns = [
    # sets the url path to home page index.html.
    path('', views.games_home, name='games_home'),
    path('create/', views.add_games, name='add_games'),
    path('details/', views.details_games, name='games_details'),
    path('<int:pk>/games_info/', views.games_info, name="games_info"),
]