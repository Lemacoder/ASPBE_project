# holdingMainMenu/utils.py

import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from HoldingMainMenu.models import Venues

def get_venue_embedding(venue):
    """Возвращает эмбеддинг площадки как список чисел"""
    return json.loads(venue.embedding)

def find_similar_venues(venue_id, top_n=5):
    """
    Находит top_n самых похожих площадок по описанию (по эмбеддингу)
    :param venue_id: id площадки, для которой ищем похожие
    :param top_n: сколько площадок вернуть
    :return: список объектов Venues
    """
    # Получаем целевую площадку и её эмбеддинг
    target = Venues.objects.get(id=venue_id)
    target_embedding = get_venue_embedding(target)

    # Получаем все остальные площадки
    venues = list(Venues.objects.exclude(id=venue_id))
    venues_embeddings = [get_venue_embedding(v) for v in venues]

    # Считаем косинусное сходство
    similarities = cosine_similarity([target_embedding], venues_embeddings)[0]

    # Сортируем по убыванию сходства и выбираем топ-N
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    return [venues[i] for i in top_indices]



"""
import json
import numpy as np
from django.contrib.auth.models import User
from .models import Venues, UserAction

def get_user_interest_vector(user):
    liked_venues = Venues.objects.filter(
        useraction__user=user,
        useraction__action_type='like'
    )
    if not liked_venues.exists():
        liked_venues = Venues.objects.filter(
            useraction__user=user,
            useraction__action_type='view'
        )
    embeddings = [json.loads(v.embedding) for v in liked_venues]
    if embeddings:
        return np.mean(embeddings, axis=0)
    return None
"""