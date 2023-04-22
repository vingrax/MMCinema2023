from datetime import date
import csv
from django.shortcuts import render,get_object_or_404,redirect
from .models import InputTable,Places,Location,Theater,Screen,DailyInputs
from django.db.models import Max
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from dal import autocomplete
from django.db.models import Lookup
from django.db.models import Field


class NotEqual(Lookup):
    lookup_name = 'ne'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <> %s' % (lhs, rhs), params
Field.register_lookup(NotEqual)




# Create your views here.
@staff_member_required
def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="shows.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Editions','Date','PlaceName', 'Theater Name','Spread','Theater Sub','Old Theater Name','Screen No','No Show','FilmName', 'Language', 'Time','Contact No','Ticket Booking'])
    return response


def uploadHandler(request):
    if request.method == 'POST':
        films = request.POST.getlist('film_name')
        languages = request.POST.getlist('language')
        show_times = request.POST.getlist('show_time')        
        screen_id = request.POST.get('screen_id')
        theater_id = request.POST.get('theater_id')
        i=0
        for film in films:
            film_name = film
            language = languages[i]
            show_time = show_times[i]

            # Set all previous DailyInputs with same screen_id to current=False
            DailyInputs.objects.filter(date__ne=date.today()).update(current=False)
            
            # Create new DailyInputs instance and save to database
            daily_input = DailyInputs(film_name=film_name, language=language, show_times=show_time, screen_id_id=screen_id, theater_id_id=theater_id, current=True,date=date.today())
            daily_input.save()
            i+=1

    return redirect('dashboard')
            
            
# def get_places(request, location_id):
#     places = Places.objects.filter(location_id=location_id).values('id', 'name')
#     return JsonResponse(list(places), safe=False) 

    

def dashboardView(request):
    context = {}
    locations = Location.objects.all()
    selected_location_id=1
    selected_place_id=208   

    if 'location' in request.POST:
        selected_location_id = request.POST.get('location')
    if 'place' in request.POST:
        selected_place_id = request.POST.get('place')
        

    defplace = Places.objects.get(id=selected_place_id)
    theaters = Theater.objects.filter(place=selected_place_id)
    defloc = Location.objects.get(id=selected_location_id)        
    places = Places.objects.filter(location=selected_location_id)
    context = {
        'theaters': theaters,
        'defloc' : defloc,
        'defplace' : defplace,
        'locations' : locations,
        'selected_location_id' : selected_location_id,
        'selected_place_id' : selected_place_id,
        'places' : places
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


        return qs