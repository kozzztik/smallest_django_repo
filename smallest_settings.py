from django import urls
from django.http import HttpResponse

ALLOWED_HOSTS = ['127.0.0.1']

def home(_):
    return HttpResponse('Hello world from mini Django!')


ROOT_URLCONF = (
    urls.re_path(r'^$', home, name='home'),
)
