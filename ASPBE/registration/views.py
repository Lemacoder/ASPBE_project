from django.shortcuts import render

from .forms import AddUser
# Create your views here.



def login(request):
    return render(request, 'log.html')

def registr(request):
    if request.method == 'POST':
        form = AddUser(request.POST,  request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = AddUser()
    return render(request, 'reg.html', {'form': form})

def log_in(request):
    return render(request, 'log_in.html')


def rec_pass_code(request):
    return render(request, 'password_recovery_code.html')



def rec_pass(request):
    return render(request, 'password_recovery.html')



#Авторизация делаем проверку по acount_type и раскидываем по приложениям  
# пользователи в User Main holding 
