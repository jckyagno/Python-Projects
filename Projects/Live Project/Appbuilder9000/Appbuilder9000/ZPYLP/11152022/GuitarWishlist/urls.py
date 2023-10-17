from django.urls import path
from . import views

urlpatterns = [
    path('', views.guitar_wishlist_home, name='GuitarWishlist_home'),
    path('create/', views.guitar_wishlist_create, name='GuitarWishlist_create'),
    path('<int:pk>/edit/', views.guitar_wishlist_edit, name='GuitarWishlist_edit'),
    path('viewall/', views.guitar_wishlist_viewall, name='GuitarWishlist_viewall'),
    path('<int:pk>/details/', views.guitar_wishlist_details, name='GuitarWishlist_details'),
    path('<int:pk>/delete/', views.guitar_wishlist_delete, name='GuitarWishlist_delete'),
    path('bs/', views.guitar_wishlist_bs, name='GuitarWishlist_bs'),
]