from django.urls import path
from . import views

urlpatterns = [
    path("dowload/<int:location_id>",views.download_csv,name='dwldcsv'),
    path("",views.downloadView,name="csv")
]
