from django.urls import path
from . import views


urlpatterns = [
    path('', views.crypto_home, name='Crypto_Home'),
    path('AddCrypto/', views.crypto_addcrypto, name='crypto_add_crypto'),
    path('Ratings/', views.crypto_ratings, name='crypto_ratings'),
    path('<int:pk>/Details/', views.crypto_details, name='crypto_details'),
    path('<int:pk>/Update/', views.crypto_update, name='crypto_update'),
    path('<int:pk>/Delete/', views.crypto_delete, name='crypto_delete'),
]