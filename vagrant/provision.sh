#!/bin/bash

PROJECT_NAME=$1

PROJECT_DIR=/vagrant
DJANGO_DIR=$PROJECT_DIR/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/venv

PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip


# Create database
su - vagrant -c "createdb $PROJECT_NAME"


# Install PIP requirements
su - vagrant -c "$PIP install -r $PROJECT_DIR/requirements.txt"


# Set execute permissions on manage.py as they get lost if we build from a zip file
chmod a+x $DJANGO_DIR/manage.py


# Run migrate/update_index
su - vagrant -c "$PYTHON $DJANGO_DIR/manage.py migrate --noinput && \
                 $PYTHON $DJANGO_DIR/manage.py update_index"


# Add a couple of aliases to manage.py into .bashrc
cat << EOF >> /home/vagrant/.bashrc
alias dj="$PYTHON $DJANGO_DIR/manage.py"
alias djrun="dj runserver 0.0.0.0:8000"
EOF
