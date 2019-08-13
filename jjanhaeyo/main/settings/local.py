from .base import *
from os import environ
import sys

DEBUG = True

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE.insert(3, 'debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'NAME': environ.get('JJANHAEYO_DB_NAME', 'jjanhaeyo'),
        'USER': environ.get('JJANHAEYO_DB_USER', 'root'),
        'PASSWORD': environ.get('JJANHAEYO_DB_PASSWORD', ''),
        'HOST': environ.get('JJANHAEYO_DB_HOST', 'localhost'),
        'PORT': environ.get('JJANHAEYO_DB_PORT', '3306'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        }
    },
    'loggers': {
        'default': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}

try:
    from .local_settings import *
except ImportError:
    pass
