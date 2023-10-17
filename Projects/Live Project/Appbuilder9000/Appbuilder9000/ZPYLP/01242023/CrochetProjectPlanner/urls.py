from django.contrib import admin
from . import views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.crochet_home, name='crochet_home'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects_page/', views.display_project, name='projects_page'),
    path('<int:pk>/details/', views.details, name='details_page'),
    path('<int:pk>/edit_project/', views.edit_project, name='edit_project'),
    path('<int:pk>/delete_project', views.delete_project, name='delete_project'),
    path('crochet_bs/', views.crochet_bs, name='crochet_bs'),
    path('crochet_api', views.crochet_api, name='crochet_api'),
]
