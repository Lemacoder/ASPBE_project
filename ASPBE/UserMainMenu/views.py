from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from HoldingMainMenu.models import Venues, Photos

# Create your views here.


def mainpage(request):
    posts = Venues.objects.filter(status=1)
    photos = Photos.objects.all()
    return render(request, 'Users/usermain.html', {'photos': photos, 'posts': posts})


def placepage(request, venid):
    posts = Venues.objects.filter(id=venid)
    post = posts.first()
    post_name = post.name
    return render(request, 'Users/page.html', {'post': post, 'title': post_name})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена </h1>')