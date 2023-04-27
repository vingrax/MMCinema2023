from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboardView,name='dashboard'),
    path('upload/',views.uploadHandler,name='uploadHandle'),
    path('item_autocomplete/', views.PlaceAutocompleteView.as_view(), name='place_autocomplete')
]
