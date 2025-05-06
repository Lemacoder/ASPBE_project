from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from HoldingMainMenu.models import Venues, Photos, UserAction,  Services, VenueService, VenueTags
import json
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def save_user_data(request):
    try:
        data = json.loads(request.body)
        print(f"Полученные данные: {data['venue_id']} - {data['action_type']}")

        if isinstance(data['venue_id'], str):
            venue = Venues.objects.get(name=data['venue_id'])
            venue_id = venue.id
            data['venue_id'] = venue_id
        

        UserAction.objects.create(
            venue_id=data['venue_id'],
            action_type=data['action_type'],
            user=request.user
        )
        return JsonResponse({'status': 'success'})
    except Exception as e:
        print(f"Ошибка: {e}")
        return JsonResponse({'status': 'error', 'message': str(e)})
