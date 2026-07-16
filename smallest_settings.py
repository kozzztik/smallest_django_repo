from django import urls
from django.http import HttpResponse


def home(_):
    return HttpResponse('Hello world from mini Django!')


ROOT_URLCONF = (
    urls.re_path(r'^$', home, name='home'),
)
