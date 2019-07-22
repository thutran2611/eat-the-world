# Settings that are unique to production go here
from .base import *  # noqa

DEBUG = True

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', 'eat-the-world.herokuapp.com'
]

INSTALLED_APPS += ['debug_toolbar']

# Add in Debug Toolbar Middleware
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE