from django.urls import path
from . import views

# the directory of . is our current directory
# so the above says import views.py from the current directory

urlpatterns = [
    path('', views.Dogs_home, name='Dogs_home'),
    path('create/', views.Dogs_create, name='create'),
    path('display/', views.display_dogs, name='lists'),
    path('<int:pk>/details/', views.details_dogs, name='details'),
    path('<int:pk>/delete/', views.delete_dog, name='delete'),
    path('confirmedelete/', views.confirm_delete, name='confirmed'),

]
