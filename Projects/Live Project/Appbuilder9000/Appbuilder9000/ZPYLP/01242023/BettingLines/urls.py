from django.urls import path
from . import views
#url patterns
urlpatterns = [
    path('', views.BettingLinesHome, name='BettingLinesHome'),
    path('add/', views.BettingLines_Add, name='BettingLines_Add'),
    path('view/', views.BettingLines_View, name='BettingLines_View'),
    path('<int:pk>/details/', views.BettingLines_Details, name='BettingLines_Details'),
    path('<int:pk>/edit/', views.BettingLines_Edit, name='BettingLines_Edit'),
    path('<int:pk>/delete/', views.BettingLines_Delete, name='BettingLines_Delete'),

]
