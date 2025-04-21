from .views import mainpage, placepage
from django.urls import path
from analythic.views import save_user_data
from associative_rules.views import services


urlpatterns = [
    path('', mainpage, name='catalog_mainpage'),
    path('Venue/<int:venid>/', placepage, name='catalog_placepage'),
    path('save_data/', save_user_data, name='save_data'),
    path('services/<int:venid>', services, name='servises')
]