from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from .models import *


menu = [
    {'title': 'About in site', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Join', 'url_name': 'login'}
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})


def addpage(request):
    return HttpResponse('Add new page')


def login(request):
    return HttpResponse('Join in')


def contact(request):
    return HttpResponse('About us')


def show_post(request, post_id):
    return HttpResponse(f'Show article to id {post_id}')


def page_not_found(request, exception):
    """
    Обработчик 404
    """
    return HttpResponseNotFound('<h1>404 Page no found</h1>')

