from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookRatings_home, name='BookRatings_home'),
    path('AddBook/', views.BookRatings_Add_Book, name='BookRatings_Add_Book'),
    path('Ratings/', views.BookRatings_Ratings, name='BookRatings_Ratings'),
    path('<int:pk>/Details/', views.BookRatings_Details, name='BookRatings_Details'),
]