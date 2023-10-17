from django.urls import path
from . import views


urlpatterns = [
    path('', views.CFB_Home, name='CFB_Home'),
    path('CreateFan/', views.CFB_AddFan, name='CFB_Add_Fan'),
    path('DisplayFans/', views.CFB_FanList, name='CFB_Fan_List'),
    path('FanDetails/<int:pk>', views.CFB_FanDetails, name='Fan_Details'),
]