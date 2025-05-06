from django import forms
from .models import Venues

class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venues
        fields = ['name', 'description', 'location', 'capacity', 'square', 'wardrobe', 'parking', 'venue_tag', 'holding_id']


