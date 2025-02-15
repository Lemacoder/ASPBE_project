from django.shortcuts import render
from .models import Venues

from .forms import AddVenueForm


def mainpagehold(request):
    posts = Venues.objects.all()
    if request.method == 'POST':
        form = AddVenueForm(request.POST,  request.FILES)
        if form.is_valid():        
            form.save() 
    else:
        form = AddVenueForm()
    return render(request, 'Holdings/holdingmain.html', {'form': form, 'posts': posts})

