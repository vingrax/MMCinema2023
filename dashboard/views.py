from datetime import date, timedelta

import json
from django.shortcuts import render,get_object_or_404,redirect
from .models import InputTable,Places,Location,Theater,Screen,DailyInputs
from django.db.models import Max
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required,permission_required
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

def updateCurrent(date):    
    currentFilms = DailyInputs.objects.filter(current=True).filter(date__ne=date)
    if currentFilms:
        for film in currentFilms:
            DailyInputs.objects.filter(id=film.id).update(current=False)
            daily_input = DailyInputs(film_name=film.film_name, language=film.language, show_times=film.show_times, screen_id_id=film.screen_id_id, theater_id_id=film.theater_id_id, current=True,date=date)
            daily_input.save()




# Create your views here.
def uploadHandler(request):
    if request.method == 'POST':
        updateCurrent(date.today()+ timedelta(days=1))
        films = request.POST.getlist('film_name')
        languages = request.POST.getlist('language')
        show_times = request.POST.getlist('show_time')        
        screen_id = request.POST.get('screen_id')
        theater_id = request.POST.get('theater_id')
        if films:
            i=0
            # Set all previous DailyInputs with same screen_id to current=False
            
            DailyInputs.objects.filter(screen_id_id=screen_id).update(current=False)
            for film in films:
                language = languages[i]
                show_time = show_times[i]                     
                # Create new DailyInputs instance and save to database
                daily_input = DailyInputs(film_name=film, language=language, show_times=show_time, screen_id_id=screen_id, theater_id_id=theater_id, current=True,date=date.today()+ timedelta(days=1))
                daily_input.save()
                i+=1
        else:
            DailyInputs.objects.filter(screen_id_id=screen_id).update(current=False)
        return JsonResponse({'status': 'success'})
    else:
        # Return a 400 Bad Request response for GET requests
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
            
def get_theaters(request):
    json_data = json.loads(request.body)
    theaters = Theater.objects.filter(place_id=json_data['place_id'])
    context = {'theaters':theaters}
    return render(request,'dashboard/theaters.html',context)

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


