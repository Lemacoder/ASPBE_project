from django.shortcuts import render
from .models import Venues


def mainpagehold(request):
    posts = Venues.objects.all()
    return render(request, 'Holdings/holdingmain.html', {'posts': posts})

def addvenue(request):
    pass