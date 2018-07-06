"""
Django settings for Musculando project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import pymysql
pymysql.install_as_MySQLdb()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import djcelery 
djcelery.setup_loader()

#BROKER_URL = 'redis://localhost:6379'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'if@mvj97gw)2&nwcv9*lz$-@0i*&k2f&^3e$bv3m30=qfxa-gh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djcelery',
    'apps.Clases',
    'apps.Caja',
    'apps.Colaboradores',
    'apps.Configuracion',
    'apps.Panel',
    'apps.Proveedores',
    'apps.UserProfile',
    'apps.Socios',
    'apps.Marketing',
    'channels',
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

ROOT_URLCONF = 'Musculando.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'apps.ContextProcesor.UserProfile.ProfileContextProcesor',
                'apps.ContextProcesor.server.server_url',
                'apps.ContextProcesor.UserProfile.SocioContextProcesor',
                'apps.ContextProcesor.Estadistica.ResumenIngresos',
                'apps.ContextProcesor.Estadistica.ResumenSociosActivos',
                'apps.ContextProcesor.Estadistica.ResumenPlanes',
                'apps.ContextProcesor.liquidacion.Liquidacion',
                'apps.ContextProcesor.Presentimo.presentimo', 
                
            ],
        },
    },
]

WSGI_APPLICATION = 'Musculando.wsgi.application'


CHANNEL_LAYERS = {
 "default": {
 "BACKEND": "asgi_redis.RedisChannelLayer",
 "CONFIG": {
   "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
 },
 'ROUTING': 'Musculando.routing.channel_routing',
 },
}


BROKER_URL = 'redis://localhost:6379/0' # Al Redis Server

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"as_musculando",
        "USER":"root",
        "PASSWORD":'',
        "PORT":'',
        'HOST':"Localhost",
        },
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/Caracas'

USE_I18N = True

USE_L10N = True

USE_TZ = True


from celery.schedules import crontab
from datetime import datetime

USE_TZ = True


CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
TIME_ZONE = 'America/Caracas'

CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = TIME_ZONE

t = datetime.today()
diario = crontab(minute=0, hour=7)
mensual = crontab(minute=0, hour=0)

CELERYBEAT_SCHEDULE = {
    'desactivate-socio': {
        'task': 'apps.Socios.tasks.desactivatesocios',
        'schedule': diario,
    },
    'aguinaldo-colaborador': {
        'task': 'apps.Colaboradores.tasks.aguinaldo',
        'schedule': mensual,
    },
    'presentimo-colaborador': {
        'task': 'apps.Colaboradores.tasks.PresentimoMensualActivate',
        'schedule': mensual,
    },
}









# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'media')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

#STATIC_ROOT = "/home/multipoint/multipoint/MultiPoint/static"


EMAIL_USE_TLS = True
EMAIL_HOST = 'b7000615.ferozo.com'
EMAIL_HOST_USER = 'musculando@b7000615.ferozo.com'
EMAIL_HOST_PASSWORD = 'Adolf5454@'
EMAIL_PORT = 587

#CACHES = {'default': {
#        'BACKEND ': 'django.core.cache.backends.db.DatabaseCache',
#        'LOCATION': 'redis://localhost:6379/0',
#        'OPTIONS': {
#        'DB':1,
#        'PARSER_CLASS':'redis.connection.HiredisParser'
#        }
#    }
#}


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/0',
        'OPTIONS': {
             'DB':1,
            'PARSER_CLASS':'redis.connection.HiredisParser'
        }
    }
}