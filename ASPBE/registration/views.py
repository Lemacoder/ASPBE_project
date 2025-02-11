from django.shortcuts import render


# Create your views here.



def login(request):
    return render(request, 'log.html')

def registr(request):
    return render(request, 'reg.html')


#Авторизация делаем проверку по acount_type и раскидываем по приложениям  
# пользователи в User Main holding 
