from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),#name='home' - добавляем имя(алиас) этого марштрута, для безопасного изменения
    path('about/', about, name='about')
]
