from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.render_main, name='clip_home'),
    path('options/', views.render_options, name='options'),
    path('about', views.render_about, name='about'),
    path('admin/', admin.site.urls),
    path('data/', views.get_events, name='data'),
    path('create/', views.create_event, name='create'),
]
