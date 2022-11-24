import environ
import os
import mongoengine
from pathlib import Path

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / '.env')

mongoengine.connect(db=env("DB"), host=env("HOST"), username=env("USERNAME"), password=env("PASSWORD"))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-9(@(b4ytdv*=)8%7l&+dz73fd$4xkzrb@*61t3y47l*3oxsjtq')

DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

# ALLOWED_HOSTS = ['.railway.app','127.0.0.1']
ALLOWED_HOST = ['*']

CSRF_TRUSTED_ORIGINS = ['https://*.railway.app','https://*.127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ugofinance.urls'

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

WSGI_APPLICATION = 'ugofinance.wsgi.application'

DATABASES = {
    'default':{
            'ENGINE': 'djongo',
            'NAME': env('DB'),
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': env('URI')
            }  
        }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS =[
    os.path.join(BASE_DIR, 'static')
]



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'