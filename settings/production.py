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

# Security
X_FRAME_OPTIONS = "DENY"
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True
# SECURE_SSL_REDIRECT = True // <- commented out for heroku deployment as it causes "ERR_TOO_MANY_REDIRECTS"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_SECONDS = 3600
SECURE_REFERRER_POLICY = "same-origin"


django_heroku.settings(locals())
