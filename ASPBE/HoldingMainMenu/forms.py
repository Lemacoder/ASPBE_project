from django import forms
from .models import Venues

class AddVenueForm(forms.ModelForm):
    class Meta:
        model = Venues
        fields = '__all__'


