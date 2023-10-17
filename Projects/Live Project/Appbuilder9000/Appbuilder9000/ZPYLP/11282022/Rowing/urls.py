from django.urls import path
from . import views

urlpatterns = [
    path('', views.rowing_home, name='rowing_home'),
    path('rowing_create/', views.rowing_create, name='rowing_create'),
    path('rowing_read/', views.rowing_read, name='rowing_read'),
    path('<int:pk>/rowing_details/', views.rowing_details, name='rowing_details'),
    path('<int:pk>/rowing_update/', views.rowing_update, name='rowing_update'),
    path('<int:pk>/rowing_delete/', views.rowing_delete, name='rowing_delete'),
    path('bs/', views.rowing_bs, name='rowing_bs'),
    path('api/', views.rowing_api, name='rowing_api'),
    path('<int:m>/rowing_save_api/', views.rowing_save_api, name='rowing_save_api'),
]
