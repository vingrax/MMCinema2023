from datetime import date, timedelta

import json
from django.shortcuts import render,get_object_or_404,redirect
from .models import Places,Location,Theater,DailyInputs,Screen
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
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

from django.db.models import Count

def create_screens():
    # get all theaters with no screens
    theaters = Theater.objects.annotate(num_screens=Count('thrscreen')).filter(num_screens=0)
    # iterate over each theater
    for theater in theaters:
        # get the number of screens required
        num_screens = int(theater.screens)
        # create screens
        for i in range(num_screens):
            # create screen with name "Screen 1", "Screen 2", etc.
            screen_name = f"Screen {i+1}"
            Screen.objects.create(name=screen_name, theater=theater)
                                  
def updateCurrent(date):    
    daily_inputs=[]
    currentFilms = DailyInputs.objects.filter(current=True).filter(date__ne=date)
    if currentFilms:
        for film in currentFilms:
            DailyInputs.objects.filter(id=film.id).update(current=False)
            daily_input = DailyInputs(film_name=film.film_name, language=film.language, show_times=film.show_times, screen_id_id=film.screen_id_id, theater_id_id=film.theater_id_id, current=True,date=date)
            daily_inputs.append(daily_input)
        # Save all DailyInputs instances to database in a single query
        DailyInputs.objects.bulk_create(daily_inputs)


def uploadHandler(request):
    if request.method == 'POST':
        tomorrow = date.today() + timedelta(days=1)
        updateCurrent(tomorrow)
        theater_id = request.POST.get('theater_id')
        # Set all previous DailyInputs with same theater_id to current=False
        DailyInputs.objects.filter(theater_id_id=theater_id, current=True).update(current=False)
        # Create list of DailyInputs instances to be saved
        daily_inputs = []
        # Iterate through the screens in the theater
        for screen in Theater.objects.get(id=theater_id).thrscreen.all():
            screen_id = screen.id
            films = request.POST.getlist(f'film_name_{screen_id}')
            languages = request.POST.getlist(f'language_{screen_id}')
            show_times = request.POST.getlist(f'show_time_{screen_id}')
            if films:
                for i in range(len(films)):
                    film = films[i]
                    language = languages[i]
                    show_time = show_times[i]
                    daily_input = DailyInputs(film_name=film, language=language, show_times=show_time, screen_id_id=screen_id, theater_id_id=theater_id, current=True, date=tomorrow)
                    daily_inputs.append(daily_input)
        # Save all DailyInputs instances to database in a single query
        DailyInputs.objects.bulk_create(daily_inputs)
        return JsonResponse({'status': 'success'})



 
            
def get_theaters(request):
    json_data = json.loads(request.body)
    theaters = Theater.objects.filter(place_id=json_data['place_id'])
    context = {'theaters':theaters}
    return render(request,'dashboard/theaters2.html',context)

def get_places(request):
    location_id = request.GET.get('location_id')
    places = Places.objects.filter(location_id=location_id)
    data = [{'id': place.id, 'name': place.name} for place in places]
    return JsonResponse(data, safe=False)
@login_required
def dashboardView(request):   
    locations = getlocation(request.user)   
    context = {        
        'locations' : locations
    }
    return render(request,'dashboard/index2.html',context)

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
    
class TheaterAutocompleteView(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Places.objects.none()

        place = self.forwarded.get('place', None)
        if place:
            qs = Places.objects.filter(place=place)
        else:
            qs = Places.objects.none()


        return qs
def getlocation(user):
    locations=set()
    if user.has_perm('dashboard.editALP'):
        locations.add(Location.objects.get(id=1))
    if user.has_perm('dashboard.editCLT'):
        locations.add(Location.objects.get(id=2))
    if user.has_perm('dashboard.editCHN'):
        locations.add(Location.objects.get(id=3))
    if user.has_perm('dashboard.editKNR'):
        locations.add(Location.objects.get(id=4))
    if user.has_perm('dashboard.editQLN'):
        locations.add(Location.objects.get(id=5))
    if user.has_perm('dashboard.editKTM'):
        locations.add(Location.objects.get(id=6))
    if user.has_perm('dashboard.editMPM'):
        locations.add(Location.objects.get(id=7))
    if user.has_perm('dashboard.editPKD'):
        locations.add(Location.objects.get(id=8))
    if user.has_perm('dashboard.editPTA'):
        locations.add(Location.objects.get(id=9))
    if user.has_perm('dashboard.editTCR'):
        locations.add(Location.objects.get(id=10))
    if user.has_perm('dashboard.editTVM'):
        locations.add(Location.objects.get(id=11))
    return locations


