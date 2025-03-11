from .views import mainpage, placepage, save_user_data
from django.urls import path



urlpatterns = [
    path('', mainpage, name='catalog_mainpage'),
    path('Venue/<int:venid>/', placepage, name='catalog_placepage'),
    path('save_data/', save_user_data, name='save_data'),
]