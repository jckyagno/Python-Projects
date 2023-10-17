from django.urls import path
from . import views

urlpatterns = [
    path('', views.directors_home, name='directors_home'),
    path('directors_add/', views.directors_add, name='directors_add'),
    path('directors_view/', views.directors_view, name='directors_view'),
    path('<int:pk>/details/', views.directors_details, name='directors_details'),
    path('<int:pk>/edit/', views.directors_edit, name='directors_edit'),
    path('<int:pk>/delete', views.directors_delete, name='directors_delete'),
    path('directors_api', views.directors_api, name='directors_api'),
    path('directors_beautifulsoup', views.directors_beautifulsoup, name='directors_beautifulsoup'),
]
