from config.settings.base import *  # flake8: noqa

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    '*',
]

STATIC_ROOT = "/var/www/{{ project_name }}/static/"
MEDIA_ROOT = "/var/www/{{ project_name }}/media/"
