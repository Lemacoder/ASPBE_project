from django.urls import path
from .views import mainpagehold, action_statistics, get_updated_data



urlpatterns = [
    path('', mainpagehold, name='holdingmainpage'),
    path('statistic/', action_statistics, name='statistic'),
    path('api/get-updated-data/', get_updated_data, name='get_updated_data'),
]