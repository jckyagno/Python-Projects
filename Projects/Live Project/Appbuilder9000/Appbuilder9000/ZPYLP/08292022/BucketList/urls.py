from django.urls import path
from . import views

urlpatterns = [
    path('', views.BucketList_home, name='BucketList_home'),
    path('create', views.BucketList_create, name='BucketList_create'),
    path('list', views.BucketList_list, name='BucketList_list'),
    path('<int:pk>/details/', views.BucketList_details, name='BucketList_details'),
    path('<int:pk>/update/', views.BucketList_update, name='BucketList_update'),
    path('<int:pk>/delete/', views.BucketList_delete, name='BucketList_delete'),
    path('api/', views.BucketList_api, name='BucketList_api'),
]

