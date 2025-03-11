from .views import  rec_pass_code, rec_pass, special_code, RegisterUser, LoginUser, EmailVerify
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', LoginUser.as_view(), name='login'),
    path('registration', RegisterUser.as_view(), name='first_step_registr'),
    path('invalid_verify', TemplateView.as_view(template_name="login_pages/invalid_verify.html"), name='invalid_verify'),
    path('verify_email/<uidb64>/<token>', EmailVerify.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name="login_pages/confirm_email.html"), name='confirm_email'),
    path('rec_code', rec_pass_code, name='recoveringcode'),
    path('rec_pass', rec_pass, name='recoveringpass'),
    path('special_code', special_code, name='specialcode')
]