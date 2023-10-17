from django.urls import path
from . import views

urlpatterns = [
    path('', views.ffxiv_db_home, name='ffxiv_db_home'),
    path('collections/', views.collections, name='collections'),
    path('CreateCollection/', views.create_collection, name='create_collection'),
    path('item/', views.items, name='items'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('ItemAPI/', views.items_api, name='item_api'),
]
