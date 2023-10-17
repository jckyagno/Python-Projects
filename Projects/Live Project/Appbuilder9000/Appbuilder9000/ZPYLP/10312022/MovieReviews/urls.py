from django.urls import path
from . import views

urlpatterns = [
    path('', views.moviereviews_Home, name='MovieReviews_home'),
    path('add/', views.moviereviews_add, name='MovieReviews_add'),
    path('all/', views.moviereviews_all, name='MovieReviews_all'),
    path('<int:pk>/details/', views.moviereviews_details, name='details'),
    path('<int:pk>/edit/', views.moviereviews_edit, name='MovieReviews_edit'),
    path('<int:pk>/delete/', views.moviereviews_delete, name="MovieReviews_delete"),
    path('api/', views.moviereviews_api, name="MovieReviews_api"),
    path('bs/', views.moviereviews_bs, name="MovieReviews_bs"),
]
