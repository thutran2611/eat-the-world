# Settings that are unique to production go here
from .base import *  # noqa

#DEBUG = True
DEBUG = False

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())


import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
