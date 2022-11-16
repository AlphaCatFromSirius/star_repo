from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import *


menu = ['About the site', 'Add article', 'Feedback', 'Join']


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})


def categories(request, cat_id):
    """
    Получение параметров переданных в GET /categories/100/?name=Ardiano&last_name=Chelentano,
    можно работать как со словарем
    """
    print(request.GET)
    return HttpResponse(f'<h1>Category page</h1><p>{cat_id}</p>')


def archive(request, year):
    """
    ВЫполняет редирект на главную, если year > 2022,
    в качестве маршрута указываем имя(алиас), определённый в urls.py приложения
    """
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1>Archives</h1><p>{year}</p>')


def page_not_found(request, exception):
    """
    Обработчик 404
    """
    return HttpResponseNotFound('<h1>404 Page no found</h1>')

