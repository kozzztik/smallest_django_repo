FROM python:3.13

EXPOSE 8000
WORKDIR /opt/
ENV DJANGO_SETTINGS_MODULE=settings

RUN pip install setuptools==81.0.0 gunicorn==23.0.0 django==6.0.7
ADD . .

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "django.core.wsgi:get_wsgi_application()"]
#CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "settings:get_application()"]
