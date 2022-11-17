from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render

from .models import *


def index(request):
    posts = Women.objects.all()

    context = {
        'cat_selected': 0,
        'posts': posts,
        'title': 'Main page'
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'About site'})


def addpage(request):
    return HttpResponse('Add new page')


def login(request):
    return HttpResponse('Join in')


def contact(request):
    return HttpResponse('About us')


def show_post(request, post_id):
    return HttpResponse(f'Show article to id {post_id}')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'cat_selected': cat_id,
        'posts': posts,
        'title': 'Category display'
    }

    return render(request, 'women/index.html', context=context)


def page_not_found(request, exception):
    """
    Обработчик 404
    """
    return HttpResponseNotFound('<h1>404 Page no found</h1>')

