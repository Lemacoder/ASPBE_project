from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from .views import RegisterView, LoginView, ActivateEmailView, logout_view, CustomTwoFactorRedirectView


app_name = 'registration'


urlpatterns = [
    #path('two_factor/', include(('two_factor.urls', 'two_factor'), namespace='two_factor')),
    #path('two_factor/redirect/', CustomTwoFactorRedirectView.as_view(), name='custom_two_factor_redirect'),
    path("", LoginView.as_view(template_name='registr/login.html'), name="login"),
    path("register/",RegisterView.as_view(),name="register"),
    path("logout/", logout_view, name='logout'),
    path("activate/<uidb64>/<token>", ActivateEmailView, name="activate"),
    

]

