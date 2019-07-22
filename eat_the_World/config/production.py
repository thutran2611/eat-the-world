# Settings that are unique to production go here
from .base import *  # noqa

DEBUG = False

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())

ALLOWED_HOSTS = [‘0.0.0.0’, ‘localhost’, ‘eat-the-world.herokuapp.com’]