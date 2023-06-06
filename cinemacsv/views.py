import csv
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from datetime import timedelta
from dashboard.models import DailyInputs,Theater,Edition,Location,Spread,Screen,Places
from django.db.models import Count


# Create your views here.
def generate_csv(location_id,date):
    location = Location.objects.get(pk=location_id)
    date=date
    filename = f"{location.unitName}.csv"
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'att achment; filename="{filename}"'
    editions = Edition.objects.filter(location_id=location_id)       
    writer = csv.writer(response)
    writer.writerow(['Editions','Date','PlaceName', 'Theater Name','Spread','Theater Sub','Old Theater Name','Screen No','No Show','FilmName', 'Language', 'Time','Contact No','Ticket Booking'])

    edtp={}
    for edition in editions:
        edition_places = edition.editionplaces.all()
        key=""
        for place in edition_places:
            key += f"{place.place_id},"
        if key in edtp:
            edtp[key]+=f"-{edition.name}"
        else:   
            edtp[key]= edition.name
    for key,edition_name in edtp.items():
        placeid_list = [x for x in key.split(",") if x != '']   
        for placeid in placeid_list: 
            place = Places.objects.get(id=placeid)       
            theaters = Theater.objects.filter(place_id=placeid).order_by('priority')
            for theater in theaters:
                try:
                    spread_instances = Spread.objects.filter(edt_id=edition.id).get(theater=theater.name)
                    spread = spread_instances.spread
                except Spread.DoesNotExist:
                    spread = False
                screens = Screen.objects.filter(theater=theater.id)
                for screen in screens:                                                
                    films = DailyInputs.objects.filter(screen_id_id=screen.id).filter(date=date)
                    if films:
                        noshow = 0
                        for film in films:
                            writer.writerow([edition_name,date,place.name,theater.name,spread,theater.t_sub,theater.oldtheatername,screen.name,noshow,film.film_name,film.language,film.show_times,theater.contactnumber,theater.booking])
                    else:
                        noshow = 1
                        writer.writerow([edition_name,date,place.name,theater.name,spread,theater.t_sub,theater.oldtheatername,screen.name,noshow,'ഇന്ന് പ്രദർശനമില്ല'])
    return response
                

@login_required
def downloadView(request):
    locations = Location.objects.all()
    context={
        "locations":locations
    }
    if request.method == 'POST':
        location_id=request.POST.get('location')
        date=request.POST.get('csvdate')     
        return generate_csv(location_id,date)
        
    return render(request,'cinemacsv/csvpage.html',context)