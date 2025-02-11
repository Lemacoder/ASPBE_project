from django.urls import path
from .views import mainpagehold


urlpatterns = [
    path('', mainpagehold, name='holdingmainpage'),
]