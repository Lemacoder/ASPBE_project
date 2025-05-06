from django.shortcuts import render
from .models import Venues, UserAction
from .forms import AddVenueForm

from django.http import JsonResponse
from collections import Counter



from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UserAction
from collections import Counter


# вынести в отдельный файл
# -------------------------
@api_view(['GET'])
def get_updated_data(request):
    # Получаем все действия из базы данных
    actions = UserAction.objects.all()
    
    # Подсчитываем количество каждого типа действия
    action_counts = Counter(action.action_type for action in actions)

    # Формируем ответ с метками и значениями
    response_data = {
        'labels': list(action_counts.keys()),
        'values': list(action_counts.values()),
    }

    return Response(response_data)


@api_view(['GET'])
def get_top_venues_data(request):
    # Получаем все действия из базы данных
    actions = UserAction.objects.all()
    
    # Подсчитываем количество действий для каждой площадки
    venue_activity = Counter(action.venue.name for action in actions)

    # Получаем топ-5 площадок по активности
    top_venues = venue_activity.most_common(5)

    # Формируем ответ с метками и значениями
    response_data = {
        'labels': [venue for venue, count in top_venues],
        'values': [count for venue, count in top_venues],
    }

    return Response(response_data)

def action_statistics(request):
    # Получаем все действия из базы данных
    actions = UserAction.objects.all()

    # Подсчитываем количество каждого типа действия
    action_counts = Counter(action.action_type for action in actions)

    # Преобразуем данные в формат для диаграммы
    labels = list(action_counts.keys())
    values = list(action_counts.values())

    # Получаем данные для топ-5 площадок
    venue_activity = Counter(action.venue.name for action in actions)
    top_venues = venue_activity.most_common(5)
    
    top_labels = [venue for venue, count in top_venues]
    top_values = [count for venue, count in top_venues]

    context = {
        'labels': labels,
        'values': values,
        'top_labels': top_labels,
        'top_values': top_values,
    }
    
    return render(request, 'Holdings/statistics.html', context)

#--------------------


def mainpagehold(request):
    posts = Venues.objects.all()
    if request.method == 'POST':
        form = AddVenueForm(request.POST,  request.FILES)
        if form.is_valid():     
            form.save()
    else:
        form = AddVenueForm()
    return render(request, 'Holdings/holdingmain.html', {'form': form, 'posts': posts})


def statistic(request):
    return render(request, 'Holdings/analytics.html')




def nlp_recomend(request):
    pass
