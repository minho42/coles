import os
import subprocess
from pathlib import Path

import dj_database_url
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("COLES_SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # Third party apps
    "allauth",
    "allauth.account",
    "crispy_forms",
    "crispy_tailwind",
    # Local apps
    "profiles.apps.ProfilesConfig",
    "coles.apps.ColesConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # The WhiteNoise middleware should be placed directly after the Django SecurityMiddleware and before all other middleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
                "django.template.context_processors.media",
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

WSGI_APPLICATION = "project.wsgi.application"


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "coles",
#         "USER": env("COLES_DB_USERNAME"),
#         "PASSWORD": env("COLES_DB_PASSWORD"),
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

# https://stackoverflow.com/questions/43459160/connect-django-to-live-heroku-postgres-database
# bash_command = "heroku config:get DATABASE_URL -a coles2"
# heroku_database_url = subprocess.check_output(["bash", "-c", bash_command]).decode("utf-8").replace("\n", "")
# DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True, default=heroku_database_url)

DATABASES = {}
DATABASES["default"] = dj_database_url.config(default=env("DATABASE_URL"), conn_max_age=600, ssl_require=True)


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Australia/Sydney"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "<minho42@gmail.com>"


# allauth
# https://django-allauth.readthedocs.io/en/latest/configuration.html
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"  # "mandatory", "optional", "none"
ACCOUNT_AUTHENTICATION_METHOD = "email"
# Using custom forms may ignore other allauth options set here unless handled manually in the custom forms
# ACCOUNT_FORMS = {
#     "login": "profiles.forms.LoginForm",
#     "reset_password": "profiles.forms.UserResetPasswordForm",
#     "signup": "profiles.forms.UserCreationForm",
# }

# ACCOUNT_ADAPTER = "profiles.models.CustomAccountAdapter"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 30
ACCOUNT_LOGOUT_REDIRECT_URL = "/"
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
# ACCOUNT_USERNAME_MAX_LENGTH = 30  # This is my own. Not part of allauth settings -> commented out as length is not check upon signup because username is removed from signup
ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_USERNAME_BLACKLIST = []
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False

# crispy forms
# CRISPY_TEMPLATE_PACK = "bootstrap4"
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# logout without confirmation
# Should convert GET to POST
ACCOUNT_LOGOUT_ON_GET = True

# custom user model
AUTH_USER_MODEL = "profiles.User"


CSP_DEFAULT_SRC = ("'none'",)
CSP_IMG_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'",)
