from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cryptocurrency_home, name='Cryptocurrency_home'),
    path('AddReview/', views.cryptocurrency_addreview, name='Cryptocurrency_AddReview'),
    path('Reviews/', views.cryptocurrency_reviews, name='Cryptocurrency_Reviews'),
    path('<int:pk>/Details/', views.cryptocurrency_details, name='Cryptocurrency_Details'),
    path('<int:pk>/Edit/', views.cryptocurrency_edit, name='Cryptocurrency_Edit'),
    path('<int:pk>/Delete/', views.cryptocurrency_delete, name='Cryptocurrency_Delete'),
    path('API/', views.cryptocurrency_api, name='Cryptocurrency_API'),
    path('Top/',views.cryptocurrency_top,name='Cryptocurrency_Top'),
]
