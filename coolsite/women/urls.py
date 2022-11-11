from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),#name='home' - добавляем имя(алиас) этого марштрута, для безопасного изменения
    path('categories/<slug:cat_id>/', categories),
    re_path(r'^archive/(?P<year>\d{4})/', archive),
]
