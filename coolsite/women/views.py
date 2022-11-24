from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404

from .forms import AddPostForm
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
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Add article error')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'title': 'Add article'})


def login(request):
    return HttpResponse('Join in')


def contact(request):
    return HttpResponse('About us')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_slug):
    cat = Category.objects.filter(slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat[0].id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'cat_selected': cat_slug,
        'posts': posts,
        'title': 'Category display'
    }

    return render(request, 'women/index.html', context=context)


def page_not_found(request, exception):
    """
    Обработчик 404
    """
    return HttpResponseNotFound('<h1>404 Page no found</h1>')

