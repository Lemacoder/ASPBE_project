from .views import login, registr
from django.urls import path

urlpatterns = [
    path('', login),
    path('registration', registr, name='first_step_registr')
]