from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CreateUserForm
from django.views.generic import View
from .emails import send_activation_mail
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .tokens import TokenGenerator
from django.http import HttpResponse
from django.contrib.auth import login
from .models import User

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin


class LoginFormView(LoginView):

    template_name = 'registr/login.html'
    success_url = '/'


def logout_view(request):
    logout(request)
    return redirect('index')

class RegisterView(View):


    def get(self,request):

        if not request.user.is_authenticated:

            form = CreateUserForm()

            context = {"form":form}
            return render(request,"registr/register.html",context)

        return redirect("/")


    def post(self,request):

        form = CreateUserForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            send_activation_mail(userID=str(user.id))

            return render(request,"registr/wait_email_confirmation.html",)


        context = {"form":form}
        return render(request,"registr/register.html",context)


def ActivateEmailView(request, uidb64, token):

    account_activation_token = TokenGenerator()

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'registr/email_confirmed.html')
    else:
        return HttpResponse('Activation link is invalid!')




class CustomTwoFactorRedirectView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.account_type == 1:
            return redirect("catalog_mainpage")
        return redirect("holdingmainpage")
