from django.urls import path
from . import views
# Class Based View Import
from .views import MyView, SnowmobileListView, SnowmobileCreate, SnowmobileUpdate, SnowmobileDelete, \
    SnowmobileDetailView, SearchResultsView, DealerCreate, DealerDetailView

urlpatterns = [
    path('', views.snowmobiles_home, name='snowmobiles_home'),
    path('add/', views.snowmobiles_add, name='snowmobiles_add'),
    path('all/', views.snowmobiles_all, name='snowmobiles_all'),
    path('<int:pk>/details/', views.snowmobiles_details, name='snowmobiles_details'),
    path('<int:pk>/edit/', views.snowmobiles_edit, name='snowmobiles_edit'),
    path('<int:pk>/delete/', views.snowmobiles_delete, name='snowmobiles_delete'),
    path('confirmdelete/', views.snowmobiles_confirmed, name='snowmobiles_confirmed'),
    path('api/', views.snowmobiles_api, name='snowmobiles_api'),
    path('bs/', views.snowmobiles_bs, name='snowmobiles_bs'),
    path('<int:m>/save_api', views.snowmobiles_save_api, name='snowmobiles_save_api'),
    path('places/', MyView.as_view(), name='snowmobile-places'),
    path('list/', SnowmobileListView.as_view(), name='snowmobile-list'),
    path('create/', SnowmobileCreate.as_view(), name='snowmobile-create'),
    path('<int:pk>/update/', SnowmobileUpdate.as_view(), name='snowmobile-update'),
    path('<int:pk>/delete_item/', SnowmobileDelete.as_view(), name='snowmobile-delete'),
    path('<int:pk>/detail_item/', SnowmobileDetailView.as_view(), name='snowmobile-detail'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('dealer_create/', DealerCreate.as_view(), name='dealer-create'),
    path('<int:pk>/detail_dealer/', DealerDetailView.as_view(), name='dealer-detail'),
]
