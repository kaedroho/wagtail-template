import os
import dj_database_url


# Basic settings

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') or []


# Database

DATABASE_URL = os.environ.get('DATABASE_URL', None)

if not DATABASE_URL:
    POSTGRES_IP = os.environ.get('POSTGRES_PORT_5432_TCP_ADDR', None)

    if POSTGRES_IP:
        POSTGRES_PORT = os.environ.get('POSTGRES_PORT_5432_TCP_PORT')
        POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
        POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', '')
        POSTGRES_DB = os.environ.get('POSTGRES_DB', '{{ project_name }}')

        POSTGRES_AUTH = POSTGRES_USER
        if POSTGRES_PASSWORD:
            POSTGRES_AUTH += ':' + POSTGRES_PASSWORD

        DATABASE_URL = 'postgres://%s@%s:%s/%s' % (
            POSTGRES_AUTH,
            POSTGRES_IP,
            POSTGRES_PORT,
            POSTGRES_DB,
        )

    else:
        # Fallback to SQLite
        # Note: any database operations performed against this SQLite file will
        # not be perisisted between commands.
        DATABASE_URL = 'sqlite://{{ project_name }}.db'

DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL),
}


# Elasticsearch

ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL', None)

if ELASTICSEARCH_URL:
    ELASTICSEARCH_INDEX = os.environ.get('ELASTICSEARCH_INDEX', '{{ project_name }}')

    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
            'URLS': [ELASTICSEARCH_URL],
            'INDEX': ELASTICSEARCH_INDEX,
        }
    }
else:
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.wagtailsearch.backends.db.DBSearch',
        }
    }


# Redis

REDIS_URL = os.environ.get('REDIS_URL', None)

if REDIS_URL:
    REDIS_KEY_PREFIX = os.environ.get('REDIS_KEY_PREFIX', '{{ project_name }}')

    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.cache.RedisCache',
            'LOCATION': REDIS_URL,
            'KEY_PREFIX': REDIS_KEY_PREFIX,
            'OPTIONS': {
                'CLIENT_CLASS': 'redis_cache.client.DefaultClient',
            }
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }

