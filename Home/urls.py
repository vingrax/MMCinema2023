from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from .forms import MyLoginView

urlpatterns = [
    path('',views.homeView,name='home'),
    path('login/',MyLoginView.as_view(template_name='Home/login.html'),name='login'),
    path('logout/',views.logout_view,name='logout')
    
]
