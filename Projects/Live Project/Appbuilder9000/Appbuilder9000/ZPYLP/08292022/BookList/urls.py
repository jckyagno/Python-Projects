from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList_Home, name='BookList_Home'),
    path('Book_Entry/', views.Book_Entry, name='BookList_Create'),
    path('Book_Display/', views.BookList_Display, name='BookList_Display'),
    path('Details/', views.BookList_Details, name='BookList_Details'),
    path('<int:pk>/Details/', views.BookList_Details, name='BookList_Details'),
    path('<int:pk>/Update/', views.BookList_Update, name='BookList_Update'),
    path('<int:pk>/Delete/', views.BookList_Delete, name='BookList_Delete'),
    path('api/', views.BookList_api, name='BookList_api'),
]