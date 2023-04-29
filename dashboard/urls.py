from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboardView,name='dashboard'),
    path('upload/',views.uploadHandler,name='uploadHandle'),
    path('get-places/', views.get_places, name='get-places'),
    path('get-theaters/', views.get_theaters, name='get-theaters'),
    path('item_autocomplete/', views.PlaceAutocompleteView.as_view(), name='place_autocomplete')
]
