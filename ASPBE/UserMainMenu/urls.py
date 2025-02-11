from .views import mainpage, placepage
from django.urls import path

urlpatterns = [
    path('', mainpage, name='catalog_mainpage'),
    path('Venue/<int:venid>/', placepage, name='catalog_placepage'),
]