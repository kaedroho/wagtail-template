import os
import dj_database_url


# Basic settings

SECRET_KEY = os.environ.get('SECRET_KEY')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',') or []


# Database

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite://{{ project_name }}.db')

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

