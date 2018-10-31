import os

import dj_database_url
import raven

from .base import *

DEBUG = TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config(conn_max_age=600)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': os.environ.get('BONSAI_URL'),
        'INDEX_NAME': 'haystack-prod',
    },
}

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'sslify.middleware.SSLifyMiddleware',
] + MIDDLEWARE

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT'))
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')

MEDIA_ROOT = '/srv/pydotorg/media'

PEP_REPO_PATH = '/srv/pydotorg/peps'

# Fastly API Key
FASTLY_API_KEY = os.environ.get('FASTLY_API_KEY')

SECURE_PROXY_SSL_HEADER = ('HTTP_FASTLY_SSL', '1')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

INSTALLED_APPS += [
    "raven.contrib.django.raven_compat",
]

RAVEN_CONFIG = {
    "dsn": os.environ.get('SENTRY_DSN'),
    "release": os.environ.get('SOURCE_VERSION'),
}
