from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, View
from .utils import *
from django.views import View

from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse


from django.contrib.auth.decorators import login_required


User=get_user_model()

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login_pages/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        combined_context = dict(list(context.items()) + list(c_def.items()))        
        return combined_context

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)  # Авторизуем пользователя
        return super().form_valid(form)


class RegisterUser(View):
    template_name = 'login_pages/reg.html'
    
    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
        
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account_type = form.cleaned_data.get('account_type')
            user = authenticate(username=username, password=password)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
            login(request, user)
            
            if account_type == 1:
                return redirect('catalog_mainpage')
            else: 
                return redirect('holdingmainpage')
            
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
        

class EmailVerify(View):
    
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)
    
        if self.user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return redirect('catalog_mainpage')
        return redirect('invalid_verify')



    @staticmethod
    def det_user(uidb64):
        try:
            uid = urlsafe_base64_decode(iudb64).decode()
            user = User.object.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
            user = None
        return user

def rec_pass_code(request):
    return render(request, 'login_pages/password_recovery_code.html',  {'title': 'Восстановления пароля', 'subtitle': 'Код для восстановления пароля был отправлен на почту', 'next_step': 'recoveringpass'})

def special_code(request):
    return render(request, 'login_pages/password_recovery_code.html',  {'subtitle': 'На указанную вами почту был отправлен код подтверждения.Введите его в данное поле.', 'next_step': 'login'})



def rec_pass(request):
    return render(request, 'login_pages/password_recovery.html')



#Авторизация делаем проверку по acount_type и раскидываем по приложениям  
# пользователи в User Main holding 

