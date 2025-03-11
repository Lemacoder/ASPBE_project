import random
from django.core.management.base import BaseCommand
from HoldingMainMenu.models import Venues, Holding  # Замените 'your_app' на имя вашего приложения


#python manage.py fill_venues

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        holding_id = Holding.objects.get(id=1)  # Получаем объект Holding с id=1

        # Создаем список площадок с данными
        venues_data = [
    {
        'name': 'Гармония',
        'description': 'Уютная площадка для проведения свадеб и корпоративов.',
        'location': 'Центр города, ул. Ленина, 10',
        'capacity': 120,
        'square': 250,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': 'Парк Сказок',
        'description': 'Идеальное место для семейных праздников и детских мероприятий.',
        'location': 'Пр. Мира, 45',
        'capacity': 80,
        'square': 150,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': 'Клуб "Атмосфера"',
        'description': 'Современный клуб для вечеринок и концертов.',
        'location': 'Ул. Молодежная, 5',
        'capacity': 300,
        'square': 500,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': 'Зал "Светлая мечта"',
        'description': 'Комфортабельный зал для конференций и семинаров.',
        'location': 'Ул. Пушкина, 12',
        'capacity': 100,
        'square': 200,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': 'Сад "Летний вечер"',
        'description': 'Идеальное место для пикников и открытых мероприятий.',
        'location': 'Парковая улица, 8',
        'capacity': 150,
        'square': 300,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Мир искусства"',
        'description': 'Выставочный зал для художественных выставок и культурных мероприятий.',
        'location': 'Ул. Культуры, 3',
        'capacity': 200,
        'square': 400,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Экоцентр"',
        'description': 'Площадка для экологических мероприятий и мастер-классов.',
        'location': "Ул. Природы, д.7",
        'capacity': 60,
        'square': 120,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Творческая мастерская"',
        'description': "Место для проведения творческих встреч и мастер-классов.",
        "location": "Ул. Ремесленная, д.4",
         "capacity": 50,
         "square": 80,
         "wardrobe": random.choice([0, 1]),
         "parking": random.choice([0, 1]),
         "status": 1
     },
     {
         "name": '"Спортивный комплекс"',
         "description": "Многофункциональная площадка для спортивных мероприятий.",
         "location": "Спортивный проспект, д.2",
         "capacity": 500,
         "square": 1000,
         "wardrobe": random.choice([0, 1]),
         "parking": random.choice([0, 1]),
         "status": 1
     },
     {
         "name": '"Конференц-центр"',
         "description": "Современное пространство для бизнес-мероприятий.",
         "location": "Бизнес-центр, ул. Деловая, д.9",
         "capacity": 250,
         "square": 600,
         "wardrobe": random.choice([0, 1]),
         "parking": random.choice([0, 1]),
         "status": 1
    },
    {
        'name': 'Креативный Хаб',
        'description': 'Современное пространство для стартапов и креативных мероприятий.',
        'location': 'Ул. Инноваций, 15',
        'capacity': 80,
        'square': 150,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': 'Театр на Дерибасовской',
        'description': 'Идеальное место для театральных постановок и культурных мероприятий.',
        'location': 'Ул. Дерибасовская, 22',
        'capacity': 300,
        'square': 500,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': 'Летний Сад',
        'description': 'Открытая площадка для пикников и летних мероприятий.',
        'location': 'Садовая улица, 5',
        'capacity': 200,
        'square': 400,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Зеленая Гора"',
        'description': "Загородная площадка для активного отдыха и корпоративов.",
        'location': "Зеленая улица, д.3",
        'capacity': 150,
        'square': 300,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Солнечный берег"',
        'description': "Пляжная площадка для летних вечеринок и барбекю.",
        'location': "Берег реки, д.6",
        'capacity': 250,
        'square': 500,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Клуб Искусств"',
        'description': "Место для выставок и культурных мероприятий.",
        'location': "Ул. Артема, д.8",
        'capacity': 100,
        'square': 200,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Бизнес-центр Рубин"',
        'description': "Современное пространство для бизнес-мероприятий и конференций.",
        'location': "Ул. Бизнеса, д.12",
        'capacity': 400,
        'square': 800,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        'name': '"Лофт на Крыше"',
        'description': "Панорамная площадка с видом на город для вечеринок.",
        'location': "Ул. Высотная, д.4",
        'capacity': 120,
        'square': 250,
        'wardrobe': random.choice([0, 1]),
        'parking': random.choice([0, 1]),
        'status': 1
    },
    {
        "name": '"Арт-центр"',
        "description": "Место для творческих встреч и мастер-классов.",
        "location": "Ул. Творчества, д.9",
        "capacity": 70,
        "square": 140,
        "wardrobe": random.choice([0, 1]),
        "parking": random.choice([0, 1]),
        "status": 1
    },
    {
        "name": '"Технопарк"',
        "description": "Площадка для технологических выставок и стартапов.",
        "location": "Ул. Инноваций, д.11",
        "capacity": 300,
        "square": 600,
        "wardrobe": random.choice([0, 1]),
        "parking": random.choice([0, 1]),
        "status": 1
    },
    {
        "name": '"Семейный Центр"',
        "description": "Площадка для семейных праздников и детских мероприятий.",
        "location": "Ул. Семейная, д.5",
        "capacity": 150,
        "square": 300,
        "wardrobe": random.choice([0, 1]),
        "parking": random.choice([0, 1]),
        "status": 1
    },
    {
        "name": '"Спорткомплекс Динамо"',
        "description": "Многофункциональная спортивная площадка для мероприятий.",
        "location": "Спортивный проспект, д.7",
        "capacity": 500,
        "square": 1000,
        "wardrobe": random.choice([0, 1]),
        "parking": random.choice([0, 1]),
        "status": 1
    },
    {
        "name": '"Кинотеатр на открытом воздухе"',
        "description": "Идеальное место для просмотра фильмов под звездами.",
        "location": "Кино-парк на озере",
        "capacity": 200,
        "square": 400,
        "wardrobe": random.choice([0, 1]),
        "parking": random.choice([0, 1]),
        "status": 1
    },
    {
        "name": '"Арт-галерея"',
        "description": "'Современная галерея для выставок и культурных событий.",
        "location": "'Ул. Искусств, д.3",
        "capacity": 100,
        "square": 200,
        "wardrobe": random.choice([0, 1]), 
        "parking" : random.choice ([0, 1]), 
        "status" :  1 
    }]


        # Заполняем базу данных
        for venue in venues_data:
            Venues.objects.create(
                name=venue['name'],
                holding_id=holding_id,
                description=venue['description'],
                location=venue['location'],
                capacity=venue['capacity'],
                square=venue['square'],
                wardrobe=venue['wardrobe'],
                parking=venue['parking'],
                status=venue['status']
            )

        self.stdout.write(self.style.SUCCESS('Successfully created venues'))
