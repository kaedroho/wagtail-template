FROM kaedroho/wagtail-base

# uWSGI
RUN pip install uwsgi
ADD docker/uwsgi.ini /usr/local/app/uwsgi.ini

# Project source code
ADD {{ project_name }}/ /usr/local/app/
ADD docker/local.py /usr/local/app/{{ project_name }}/settings/local.py
ADD docker/wsgi_docker.py /usr/local/app/{{ project_name }}/wsgi_docker.py

# PIP requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/local/app
CMD uwsgi --ini uwsgi.ini
EXPOSE 80
