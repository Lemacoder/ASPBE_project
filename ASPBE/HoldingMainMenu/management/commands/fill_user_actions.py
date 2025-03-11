import random
from django.core.management.base import BaseCommand
from HoldingMainMenu.models import UserAction, Venues  

class Command(BaseCommand):
    help = 'Fill the UserAction table with random data'

    def handle(self, *args, **kwargs):
        # Получаем все площадки из базы данных
        venues = Venues.objects.all()

        # Проверяем, есть ли площадки
        if not venues.exists():
            self.stdout.write(self.style.ERROR('Нет площадок в базе данных.'))
            return

        # Определяем типы действий
        action_types = ['Наведение', 'Лайк', 'Связаться', 'Нажатие']

        for _ in range(1000):  # Генерируем 100 записей
            venue = random.choice(venues)  # Случайная площадка
            action_type = random.choice(action_types)  # Случайный тип действия
            
            # Создаем запись о действии пользователя
            UserAction.objects.create(venue=venue, action_type=action_type)

        self.stdout.write(self.style.SUCCESS('Успешно добавлено 100 записей о действиях пользователей.'))
