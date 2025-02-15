from .views import login, registr, log_in, rec_pass_code, rec_pass
from django.urls import path

urlpatterns = [
    path('', login, name='login'),
    path('registration', registr, name='first_step_registr'), 
    path('log_in', log_in, name='the_code'), 
    path('rec_code', rec_pass_code, name='recoveringcode'),
    path('rec_pass', rec_pass, name='recoveringpass')
]