from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from HoldingMainMenu.models import Venues, Photos, UserAction,  Services, VenueService, VenueTags
import json
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


# Create your views here.

ACTIVE = 1

def mainpage(request):
    posts = Venues.objects.filter(status=ACTIVE)

    popular_venues = (
        UserAction.objects.filter(action_type__in=['Наведение', 'Нажатие'])
        .values('venue') 
        .annotate(total_actions=Count('id'))  
        .order_by('-total_actions')[:10]  
    )

    
    popular_venue_ids = [entry['venue'] for entry in popular_venues]
    popular_venues_details = Venues.objects.filter(id__in=popular_venue_ids)

    return render(request, 'Users/usermain.html', {'posts': posts, 'popular_venues_details':popular_venues_details})


def placepage(request, venid):
    posts = Venues.objects.filter(id=venid)
    post = posts.first()
    post_name = post.name
    return render(request, 'Users/page.html', {'post': post, 'title': post_name})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')




