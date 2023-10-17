from django.urls import path
from . import views


urlpatterns = [
    # sets the urld path to the home page thecasualgardener_home.html
    path('', views.ChristmasList_home, name='ChristmasList_home'),
    path('create/', views.gift_create, name='gift_create'),
    path('list/', views.gift_list, name='gift_list'),
    path('<int:pk>/details/', views.gift_details, name='gift_details'),
    path('<int:pk>/edit/', views.gift_edit, name='gift_edit'),
    path('<int:pk>/delete/', views.gift_delete, name='gift_delete'),
    path('api/', views.christmas_api, name='api'),
    path('bs/', views.christmas_bs, name='bs'),
    path('<str:p1>/<str:p2>/saved_api/', views.saved_api, name='saved_api'),
]