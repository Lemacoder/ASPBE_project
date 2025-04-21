from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import RegisterView, LoginView, ActivateEmailView, logout_view


app_name = "registration"

urlpatterns = [
    path("", LoginView.as_view(template_name='registr/login.html'), name="login"),
    path("register/",RegisterView.as_view(),name="register"),
    
    path("logout/", logout_view, name='logout'),
    path("activate/<uidb64>/<token>", ActivateEmailView,name="activate"),

]

