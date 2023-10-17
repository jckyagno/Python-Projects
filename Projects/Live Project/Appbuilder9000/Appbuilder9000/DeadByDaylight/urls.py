from django.urls import path
from . import views


urlpatterns = [
    path('', views.deadByDaylight_home, name="deadByDaylight_home"),
    path('killers/', views.deadByDaylight_killers, name="deadByDaylight_killers"),
    path('survivor/', views.deadByDaylight_survivors, name="deadByDaylight_survivors"),
    path('createkiller/', views.create_killer, name="deadByDaylight_createK"),
    path('createsurvivor/', views.create_survivor, name="deadByDaylight_createS"),
    path('<int:pk>/survdetails/', views.survivorDetails, name='deadByDaylight_survivor_details'),
    path('<int:pk>/killerdetails/', views.killerDetails, name='deadByDaylight_killer_details'),
    path('<int:pk>/edit/', views.deadByDaylight_edit, name='deadByDaylight_edit'),
    path('<int:pk>/kedit/', views.deadByDaylight_kedit, name='deadByDaylight_kedit'),
    path('delete/', views.deadByDaylight_delete, name='deadByDaylight_delete'),
    path('kdelete/', views.deadByDaylight_kdelete, name='deadByDaylight_kdelete'),
    path('secret/', views.deadByDaylight_secret, name="deadByDaylight_secret"),
]