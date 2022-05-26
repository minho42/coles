from .base import *
from .security import *

import django_heroku

DEBUG = False

ALLOWED_HOSTS += [
    "coles2.herokuapp.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://coles2.herokuapp.com",
]


django_heroku.settings(locals())
