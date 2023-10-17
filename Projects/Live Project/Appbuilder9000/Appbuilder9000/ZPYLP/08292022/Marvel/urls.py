from django.urls import path, include
from . import views, admin

urlpatterns = [
    path('', views.marvel_home, name='marvel_home'),
    path('create/', views.marvel_create, name='marvel_create'),
    path('roster/', views.marvel_roster, name='marvel_roster'),
    path('<int:pk>/details/', views.marvel_details, name='marvel_details'),
    path('<int:pk>/update/', views.marvel_update, name='marvel_update'),
    path('<int:pk>/delete/', views.marvel_delete, name='marvel_delete'),
    path('<int:pk>/delete_comments/details/', views.delete_comment, name='delete_comment'),
    path('api/', views.marvel_api, name='marvel_api'),
    path('bs/', views.marvel_bs, name='marvel_bs'),
    path('<combo>/saved/', views.marvel_api_saved, name='marvel_saved'),
    path('search/', views.search, name='search'),
]
