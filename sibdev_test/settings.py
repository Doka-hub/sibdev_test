"""
Django settings for sibdev_test project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

env = os.environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.get(
    'APP_SECRET_KEY',
    'django-insecure-)lza-9mgks6nid4&&9wuat74u(vgd85_ya&dwg^0#_%n=6_$@b',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get('APP_DEBUG', True)

ALLOWED_HOSTS = env.get('APP_ALLOWED_HOSTS', 'localhost 127.0.0.1').split(' ')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'drf_spectacular',
    'django_celery_beat',

    'rest_framework',
    'rest_framework_simplejwt',

    'apps.accounts.apps.AccountsConfig',
    'apps.quotes.apps.QuotesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sibdev_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sibdev_test.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DB_NAME = env.get('DB_NAME', 'sibdev_test')
DB_USER = env.get('DB_USER', 'sibdev_user')
DB_PASSWORD = env.get('DB_PASSWORD', 'sibdev_password')
DB_HOST = env.get('DB_HOST', 'localhost')
DB_PORT = env.get('DB_PORT', '5432')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'

# REDIS
REDIS_HOST = env.get('REDIS_HOST')
REDIS_PORT = env.get('REDIS_PORT')
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}'

# CELERY
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL', 'redis://redis:6379')
CELERY_RESULT_BACKEND = env.get('CELERY_RESULT_BACKEND', 'redis://redis:6379')

# REST FRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'ORDERING_PARAM': 'order_by',
}

# JWT
ACCESS_TOKEN_LIFETIME_DAYS = env.get('ACCESS_TOKEN_LIFETIME_DAYS', 30)
REFRESH_TOKEN_LIFETIME_DAYS = env.get('ACCESS_TOKEN_LIFETIME_DAYS', 60)

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=ACCESS_TOKEN_LIFETIME_DAYS),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=REFRESH_TOKEN_LIFETIME_DAYS),
    'TOKEN_OBTAIN_SERIALIZER': 'apps.accounts.serializers.CustomTokenObtainPairSerializer',
}

# CBR XML
CBR_XML_BASE_API_URL = env.get('CBR_XML_BASE_API_URL', 'https://www.cbr-xml-daily.ru')
CBR_XML_API_ENDPOINTS = {
    'archive': env.get('CBR_XML_ARCHIVE_ENDPOINT', 'archive/{year}/{month}/{day}/daily_json.js'),
    'daily': env.get('CBR_XML_DAILY_ENDPOINT', 'daily_json.js'),
}

# EMAIL
EMAIL_BACKEND = env.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_USE_TLS = env.get('EMAIL_USE_TLS', True)
EMAIL_HOST = env.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = env.get('EMAIL_PORT', 587)
EMAIL_HOST_USER = env.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = env.get('EMAIL_HOST_PASSWORD', None)
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# LOGGING

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        'console_errors': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'errors': {
            'handlers': ['console_errors'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

# SCHEMA
SPECTACULAR_SETTINGS = {
    'TITLE': 'Спецификация API для тестового задания Currencies',
    'VERSION': '1',
    'SERVE_INCLUDE_SCHEMA': False,
}
