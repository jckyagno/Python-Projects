from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #sets the url path to home page thecasualgardener_home.html
    path('', views.Pokedex_home, name='Pokedex_home'),
    #sets the url path to Create New Account page CreateNewAccount.html
    path('create_user/', views.create_user, name='create_user'),
    #sets the url path to Add Pokemon page add_pkmn.html
    path('add_pkmn/', views.add_pkmn, name='add_pkmn'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('view_pkmn/', views.view_pkmn, name='view_pkmn'),

    #path to page details while also taking to account the pokemon_name
    #path('details/', views.Pokemon_details, name='Pokemon_details'),
    path('<int:pk>/details/', views.Pokedex_details, name='Pokedex_details'),

]