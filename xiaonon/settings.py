"""
Django settings for xiaonon project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import json


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if 'LINE_CHANNEL_SECRET' in os.environ:
    pwddata = {
        "LINE_CHANNEL_ACCESS_TOKEN" : os.environ.get('LINE_CHANNEL_ACCESS_TOKEN'),
        "LINE_CHANNEL_SECRET" : os.environ.get('LINE_CHANNEL_SECRET'),
        "LINE_LOGIN_CHANNEL_ID" : os.environ.get('LINE_LOGIN_CHANNEL_ID'),
        "LINE_LOGIN_CHANNEL_SECRET" : os.environ.get('LINE_LOGIN_CHANNEL_SECRET'),
        "POSTGRES_HOST" : os.environ.get('POSTGRES_HOST'),
        "POSTGRES_PORT" : os.environ.get('POSTGRES_PORT'),
        "POSTGRES_USERNAME" : os.environ.get('POSTGRES_USERNAME'),
        "POSTGRES_PASSWORD" : os.environ.get('POSTGRES_PASSWORD'),
        "AWS_ACCESS_KEY_ID" : os.environ.get('AWS_ACCESS_KEY_ID'),
        "AWS_SECRET_ACCESS_KEY" : os.environ.get('AWS_SECRET_ACCESS_KEY'),
        "AWS_STORAGE_BUCKET_NAME" : os.environ.get('AWS_STORAGE_BUCKET_NAME')
    }
else:
    with open(os.path.join(BASE_DIR, "pwd.json"), 'r', encoding='utf8') as f:
        pwddata = json.load(f)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1v^q654^2@l1k%t0^wgy1c3_$o)0+fjsxhzcj!qb%l-y6d9(+s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'xiaonon.herokuapp.com', 
    'xiaononshop.com', 
    'xiaonon-dev.us-east-1.elasticbeanstalk.com', 
    'ogbento-dev.ap-southeast-1.elasticbeanstalk.com', 
    '127.0.0.1',
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'order.apps.OrderConfig',
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

ROOT_URLCONF = 'xiaonon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'xiaonon.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': pwddata['POSTGRES_USERNAME'],
        'PASSWORD': pwddata['POSTGRES_PASSWORD'],
        'HOST': pwddata['POSTGRES_HOST'],
        'PORT': pwddata['POSTGRES_PORT'],
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# S3 access settings
AWS_ACCESS_KEY_ID = pwddata['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = pwddata['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = pwddata['AWS_STORAGE_BUCKET_NAME']

# S3 file storage settings (user upload)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# general static settings
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# S3 static settings
STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATIC_LOCATION = 'static'  # Settings used in storages.py
STATICFILES_STORAGE = 'xiaonon.storages.StaticStorage' ## disable static_root: will directly help you collect static files to S3 when running collectstatic 
STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'  ## for accsessing static files in S3

# S3 media settings
# ENV_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# MEDIA_ROOT = os.path.join(ENV_PATH, 'media')  ## user upload to this place
# MEDIA_LOCATION = 'media'    # You should have created two folders on your bucket with these names
# DEFAULT_FILE_STORAGE = 'TPautomation.storages.MediaStorage'  ## from django.core.files.storage import default_storage
# MEDIA_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/media/'  ## seems like I have to upload my media to this url

LINE_CHANNEL_ACCESS_TOKEN = pwddata['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET = pwddata['LINE_CHANNEL_SECRET']
LINE_LOGIN_CHANNEL_ID = pwddata['LINE_LOGIN_CHANNEL_ID']
LINE_LOGIN_CHANNEL_SECRET = pwddata['LINE_LOGIN_CHANNEL_SECRET']

DOMAIN = 'https://xiaononshop.com/'
AWS_BENTO_IMG_URL = "https://s3-ap-southeast-1.amazonaws.com/ogbento/"



