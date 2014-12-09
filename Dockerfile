FROM kaedroho/wagtail-base

# Docker-specific PIP requirements
ADD docker/requirements.txt docker-requirements.txt
RUN pip install -r docker-requirements.txt

# Project source code
ADD {{ project_name }}/ /usr/local/app/

# Docker-specific configuration
ADD docker/uwsgi.ini /usr/local/app/uwsgi.ini
ADD docker/local.py /usr/local/app/{{ project_name }}/settings/local.py
ADD docker/wsgi_docker.py /usr/local/app/{{ project_name }}/wsgi_docker.py

# Project PIP requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/local/app
CMD uwsgi --ini uwsgi.ini
EXPOSE 80
