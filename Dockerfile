FROM kaedroho/wagtail-base

# PIP requirements
ADD docker/requirements.txt docker-requirements.txt
RUN pip install -r docker-requirements.txt

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Project source code
ADD {{ project_name }}/ /usr/local/app/

# Docker configuration
ADD docker/uwsgi.ini /usr/local/app/uwsgi.ini
ADD docker/local.py /usr/local/app/{{ project_name }}/settings/local.py
ADD docker/wsgi_docker.py /usr/local/app/{{ project_name }}/wsgi_docker.py
ADD docker/bin/ /usr/local/bin/

VOLUME /usr/local/static/
VOLUME /usr/local/media/
WORKDIR /usr/local/app
ENV DJANGO_SETTINGS_MODULE={{ project_name }}.settings.production
CMD uwsgi --ini uwsgi.ini
EXPOSE 80
