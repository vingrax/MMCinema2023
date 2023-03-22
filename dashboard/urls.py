from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboardView,name='dashboard'),
    path('shows/',views.showView,name='shows'),
    path('download/',views.download_csv)
]
