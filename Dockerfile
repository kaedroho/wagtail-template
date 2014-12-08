FROM kaedroho/wagtail-base

# uWSGI
RUN pip install uwsgi
ADD docker/uwsgi.ini /usr/local/django/{{ project_name }}/uwsgi.ini

# Project source code
ADD {{ project_name }}/ /usr/local/django/{{ project_name }}/
ADD docker/local.py /usr/local/django/{{ project_name }}/{{ project_name }}/settings/local.py

# PIP requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/local/django/{{ project_name }}
CMD uwsgi --ini uwsgi.ini
EXPOSE 80
