from django.urls import path
from . import views

# urls which point to function in views.py
urlpatterns = [
    path('', views.puppy_home, name='puppy_home'),
    path('time/', views.puppy_add, name='puppy_add'),
    path('list/', views.puppy_all, name='puppy_all'),
    path('<int:pk>/details/', views.puppy_details, name='puppy_details'),
    path('<int:pk>/delete/', views.puppy_delete, name='puppy_delete'),
    path('<int:pk>/update/', views.puppy_update, name='puppy_update'),
    path('bs/', views.puppy_bs, name='puppy_bs'),
]