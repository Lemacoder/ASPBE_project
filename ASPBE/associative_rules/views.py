

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from HoldingMainMenu.models import Venues, Photos, UserAction,  Services, VenueService, VenueTags
import json
from django.db.models import Count, Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# Create your views here.


def services(request, venid):
    """
    Отображает список услуг, рекомендованных для данной площадки,
    основываясь на анализе данных VenueService.
    """
    # Получаем объект площадки или возвращаем 404, если не найден
    venue = get_object_or_404(Venues, id=venid)

    # Получаем тег площадки
    venue_tag = venue.venue_tag

    # Получаем все услуги
    all_services = Services.objects.all()

    # Получаем все VenueService для данного тега площадки
    venue_services = VenueService.objects.filter(venue_tag=venue_tag)

    # Извлекаем ID услуг из VenueService
    all_service_ids_for_tag = []
    for vs in venue_services:
        all_service_ids_for_tag.extend(vs.get_services())  # get_services возвращает список ID

    # Рассчитываем confidence для каждой услуги
    service_confidences = {}
    for service in all_services:
        service_id = service.id
        # X and Y: количество раз, когда услуга встречается для данного тега
        x_and_y = all_service_ids_for_tag.count(service_id)

        # X: общее количество услуг для данного тега
        x = len(all_service_ids_for_tag)

        # Рассчитываем confidence
        if x > 0:
            confidence = (x_and_y / x) * 100
        else:
            confidence = 0.0
        service_confidences[service_id] = confidence

    # Фильтруем услуги с confidence выше 16%
    high_confidence_services = {
        service_id: confidence
        for service_id, confidence in service_confidences.items()
        if confidence > 16
    }

    # Рассчитываем support для каждой услуги с высоким confidence
    service_supports = {}
    total_venue_services = VenueService.objects.count()  # Общее количество записей в VenueService

    for service_id in high_confidence_services:
        # X and Y: количество раз, когда услуга встречается для данного тега
        x_and_y = all_service_ids_for_tag.count(service_id)

        # Все
        all_count = total_venue_services

        if all_count > 0:
            support = (x_and_y / all_count) * 100
        else:
            support = 0.0
        service_supports[service_id] = support

    # Получаем объекты Services для услуг с высоким confidence и support
    recommended_services = [] # Изменим структуру данных для удобства
    for service in Services.objects.filter(id__in=service_supports.keys()):
        recommended_services.append({
            'service': service,
            'support': service_supports[service.id]
        })

    # Передаем данные в шаблон
    context = {
        'venue': venue,
        'recommended_services': recommended_services,
    }

    return render(request, 'Users/services.html', context)