"""
Django settings for djangoblog project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path # this import standard with Django
import os
import django_on_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent  # standard with Django


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-f9*7^kz&dtfht@nu=e3--5tftz9m#xxlax4n@rajvzha&jlo-v' # secret key standard with Django
SECRET_KEY = os.environ.get('SECRET_DJANGO_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True # this set to True upon new project creation

ALLOWED_HOSTS = ['snerdblog.herokuapp.com'] # this list is empty upon new project creation


# Application definition

INSTALLED_APPS = [
    'storages',
    'crispy_forms',
    'users',
    'blog',
    'django.contrib.admin', # standard with Django
    'django.contrib.auth', # standard with Django
    'django.contrib.contenttypes', # standard with Django
    'django.contrib.sessions', # standard with Django
    'django.contrib.messages', # standard with Django
    'django.contrib.staticfiles' # standard with Django
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # standard with Django
    'django.contrib.sessions.middleware.SessionMiddleware', # standard with Django
    'django.middleware.common.CommonMiddleware', # standard with Django
    'django.middleware.csrf.CsrfViewMiddleware', # standard with Django
    'django.contrib.auth.middleware.AuthenticationMiddleware', # standard with Django
    'django.contrib.messages.middleware.MessageMiddleware', # standard with Django
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # standard with Django
]

ROOT_URLCONF = 'djangoblog.urls' # standard with Django

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # standard with Django
        'DIRS': [], # this list empty upon new project creation
        'APP_DIRS': True, # this set to to True upon new project creation
        'OPTIONS': { # standard with Django
            'context_processors': [ # this list has four items upon new project creation (see below)
                'django.template.context_processors.debug', # standard with Django
                'django.template.context_processors.request', # standard with Django
                'django.contrib.auth.context_processors.auth', # standard with Django
                'django.contrib.messages.context_processors.messages', # standard with Django
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoblog.wsgi.application' # standard with Django


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # standard with Django
        'NAME': BASE_DIR / 'db.sqlite3', # standard with Django
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # standard with Django
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # standard with Django
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # standard with Django
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # standard with Django
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us' # standard with Django

TIME_ZONE = 'UTC' # standard with Django

USE_I18N = True # standard with Django

USE_TZ = True # standard with Django


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = 'static/' # standard with Django

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # standard with Django

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_KEY_ID') # enviornment variable
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY') # enviornment variable
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')  # enviornment variable
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_REGION_NAME = 'us-east-1'

django_on_heroku.settings(locals())