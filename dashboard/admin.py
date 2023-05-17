from django.contrib import admin
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
from .models import Spread,Edition,Editionplaces,Theater,Screen,Location
from .forms import TheaterForm

admin.site.site_header = "MMCinema Administration"
admin.site.site_title = "MMCinema Admin Portal"
admin.site.index_title = "Welcome to MMCinema Administration"

# Register your models here.
class ScreenInline(admin.StackedInline):
    model = Screen
    fields = ['name']
    extra = 0

class EditionInline(admin.TabularInline):
    model = Edition
    extra = 0
class EditionplacesInline(admin.TabularInline):
    model = Editionplaces
    extra = 0

@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    inlines = [ScreenInline]
    search_fields=('name',)
    form=TheaterForm

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        ScreenFormSet = inlineformset_factory(Theater, Screen, fields=('name',))
        formset = ScreenFormSet(request.POST, instance=obj)
        if formset.is_valid():
            formset.save()
       
    
class LocationAdmin(admin.ModelAdmin):
    inlines = [EditionInline]

@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    inlines = [EditionplacesInline]



admin.site.register(Location,LocationAdmin)   
admin.site.register(Spread)



