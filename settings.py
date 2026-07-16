import functools
import pathlib

from django import urls
from django.http import HttpResponse
from django.contrib import admin


BASE_DIR = pathlib.Path(__file__).parent

DEBUG = True
USE_TZ = False
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
            ]
        }
    }
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_URL = '/static/'

(BASE_DIR / 'data').mkdir(parents=True, exist_ok=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Движок базы данных
        'NAME': BASE_DIR / 'data' / 'db.sqlite3',        # Путь к файлу базы данных
    }
}
SECRET_KEY = 'SECRET_KEY'


def home(_):
    return HttpResponse('Hello world!')


class UrlsPy:
    @functools.cached_property
    def urlpatterns(self):
        """
        Some magic here. We can not start admin panel before settings module can be loaded. So url patterns should
        be lazy loaded.
        """
        admin.autodiscover()
        return [
            urls.re_path(r'^$', home, name='home'),
            urls.re_path(r'^admin/', admin.site.urls),
            urls.re_path(r'^admin/doc/', urls.include('django.contrib.admindocs.urls')),
        ]

ROOT_URLCONF = UrlsPy()

