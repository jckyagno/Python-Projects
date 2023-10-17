from django.urls import path
from . import views

urlpatterns = [
    path('', views.bucketlist_home, name='bucketlist_home'),
    path('create/', views.bucketlist_create, name='bucketlist_create'),
    path('read/', views.bucketlist_read, name='bucketlist_read'),
    path('<int:pk>/details/', views.bucketlist_details, name='bucketlist_details'),
    path('<int:pk>/update/', views.bucketlist_update, name='bucketlist_update'),
    path('<int:pk>/delete/', views.bucketlist_delete, name='bucketlist_delete'),
]
