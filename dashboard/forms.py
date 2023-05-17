from django import forms
from dal import autocomplete
from .models import Theater,Places,Screen

class TheaterForm(forms.ModelForm):

    place = forms.ModelChoiceField(
                queryset=Places.objects.all(),
                widget=autocomplete.ModelSelect2(
                        url='place_autocomplete',
                        forward=['location']
                ),
            )
    class Meta:
        model = Theater
        fields = "__all__"

