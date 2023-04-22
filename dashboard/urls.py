from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboardView,name='dashboard'),
    path('download/',views.download_csv),
    path('upload/',views.uploadHandler,name='uploadHandle'),
    # path('get-places/<int:location_id>/', views.get_places, name='get_places'),
    path('item_autocomplete/', views.PlaceAutocompleteView.as_view(), name='place_autocomplete')
]
