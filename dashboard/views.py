import datetime
import csv
from django.shortcuts import render,get_object_or_404
from .models import InputTable,Places,Location,Theater,Screen 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from dal import autocomplete




# Create your views here.
@staff_member_required
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shows.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Editions','Date','PlaceName', 'Theater Name','Spread','Theater Sub','Old Theater Name','Screen No','No Show','FilmName', 'Language', 'Time','Contact No','Ticket Booking'])
    return response

@login_required
def showView(request):
    shows = InputTable.objects.all().filter(date=datetime.date(2023, 3, 17))
    return render(request,'dashboard/shows.html',{"shows" : shows})



def dashboardView(request):
    locations = Location.objects.all()
    selected_location_id=1
    selected_place_id=207
    if request.method == 'POST':
        selected_location_id = request.POST.get('location')
        selected_place_id = request.POST.get('place')
    screens = Screen.objects.filter(place=selected_place_id)
    defplace = Places.objects.get(id=selected_place_id)
    theaters = Theater.objects.filter(place=selected_place_id)
    defloc = Location.objects.get(id=selected_location_id)        
    places = Places.objects.filter(location=selected_location_id)
    context = {
        'theaters':theaters,
        'defloc' : defloc,
        'defplace':defplace,
        'locations':locations,
        'selected_location_id':selected_location_id,
        'selected_place_id':selected_place_id,
        'places':places,
        'screens':screens
    }
    return render(request,'dashboard/index.html',context)

class PlaceAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Places.objects.none()

        location = self.forwarded.get('location', None)
        if location:
            qs = Places.objects.filter(location=location)
        else:
            qs = Places.objects.none()
        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs