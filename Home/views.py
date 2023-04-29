from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def homeView(request):
    return render(request,'Home/frontpage.html')

def logout_view(request):
    logout(request)
    return redirect('login')

