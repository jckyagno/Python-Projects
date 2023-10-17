from django.urls import path
from . import views

# registers urlpatterns ---------------------------------------------------
urlpatterns = [
    path('', views.cl_home, name='cl_home'),
    path('create/', views.cl_create, name='cl_create'),
    path('list/', views.cl_list, name='cl_list'),
    path('<int:pk>/details/', views.cl_details, name='cl_details'),
    path('<int:pk>/update/', views.cl_update, name='cl_update'),
    path('<int:pk>/delete/', views.cl_delete, name='cl_delete'),
    path('api/', views.cl_api, name='cl_api'),
    path('bs/', views.cl_bs, name='cl_bs'),
    path('<int:m>/save_api/', views.cl_save_api, name='cl_save_api'),
]
