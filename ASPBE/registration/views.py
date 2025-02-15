from django.shortcuts import render


# Create your views here.



def login(request):
    return render(request, 'log.html')

def registr(request):
    return render(request, 'reg.html')

def log_in(request):
    return render(request, 'log_in.html')


def rec_pass_code(request):
    return render(request, 'password_recovery_code.html')



def rec_pass(request):
    return render(request, 'password_recovery.html')



#Авторизация делаем проверку по acount_type и раскидываем по приложениям  
# пользователи в User Main holding 
