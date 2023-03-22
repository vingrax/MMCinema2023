import datetime
import csv
from django.shortcuts import render,get_object_or_404
from .models import InputTable 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shows.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['hello'])
    return response


def showView(request):
    shows = InputTable.objects.all().filter(date=datetime.date(2023, 3, 17))
    return render(request,'dashboard/shows.html',{"shows" : shows})
 
def dashboardView(request):
    return render(request,'dashboard/index.html')