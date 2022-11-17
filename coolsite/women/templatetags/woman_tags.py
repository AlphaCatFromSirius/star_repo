from django import template
from women.models import *


register = template.Library()


# @register.simple_tag(name='get_cats')
# def get_categories(filter=None):
#     if not filter:
#         return Category.objects.all()
#     else:
#         return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/menu.html')
def show_menu():
    menu = [
        {'title': 'About in site', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_page'},
        {'title': 'Feedback', 'url_name': 'contact'},
        {'title': 'Join', 'url_name': 'login'}
    ]
    return {'menu': menu}


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}
