from django.urls import path
from . import views

urlpatterns = [
    path('', views.vampire_home, name='vampire_home'),
    path('vampire_entry', views.vampire_entry, name='vampire_entry'),
    path('vampire_view', views.vampire_view, name='vampire_view'),
    path('<int:pk>/vampire_details', views.vampire_details, name='vampire_details'),
    path('<int:pk>/vampire_edit', views.vampire_edit, name='vampire_edit'),
    path('<int:pk>/vampire_delete', views.vampire_delete, name='vampire_delete'),
    ]
