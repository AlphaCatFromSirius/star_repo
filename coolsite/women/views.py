from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from .models import *


menu = [
    {'title': 'About in site', 'url_name': 'about'},
    {'title': 'Add article', 'url_name': 'add_page'},
    {'title': 'Feedback', 'url_name': 'contact'},
    {'title': 'Join', 'url_name': 'login'}
]


def index(request):
    cats = Category.objects.all()
    posts = Women.objects.all()

    context = {
        'cats': cats,
        'cat_selected': 0,
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


def show_category(request, cat_id):
    cats = Category.objects.all()
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'cats': cats,
        'cat_selected': cat_id,
        'posts': posts,
        'menu': menu,
        'title': 'Category display'
    }

    return render(request, 'women/index.html', context=context)


def page_not_found(request, exception):
    """
    Обработчик 404
    """
    return HttpResponseNotFound('<h1>404 Page no found</h1>')

