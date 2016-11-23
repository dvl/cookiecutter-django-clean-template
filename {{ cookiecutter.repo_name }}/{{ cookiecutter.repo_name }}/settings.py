"""
Django settings for {{ cookiecutter.project_name }} project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse as db_url

ADMINS = (
    ('André Luiz', 'contato@xdvl.info'),
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).absolute().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'collectfast',
    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd
    'compressor',
    'debug_toolbar',
    'django_extensions',
    'storages',
    # Project
    '{{ cookiecutter.repo_name }}.core',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR / '{{ cookiecutter.repo_name }}' / 'templates'),
        ],
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

WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': '{{ cookiecutter.repo_name }}.core.middleware.show_toolbar'
}


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {'default': config('DATABASE_URL', cast=db_url)}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# AWS
# https://boto3.readthedocs.org/en/latest/

AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', '123')

AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', '456')

AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME', '{{ cookiecutter.repo_name }}')

AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN', 's3.amazonaws.com/{{ cookiecutter.repo_name }}')

AWS_PRELOAD_METADATA = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', 'django.core.files.storage.FileSystemStorage')
DEFAULT_S3_PATH = 'media'

STATICFILES_STORAGE = config('STATICFILES_STORAGE', 'django.contrib.staticfiles.storage.StaticFilesStorage')
STATIC_S3_PATH = 'static'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATICFILES_DIRS = [
    str(BASE_DIR / 'bower_components'),
    str(BASE_DIR / '{{ cookiecutter.repo_name }}' / 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR / 'media-root')

STATIC_URL = '/static/'
STATIC_ROOT = str(BASE_DIR / 'static-root')


# Django-compressor
# https://django-compressor.readthedocs.org/en/latest/

COMPRESS_PRECOMPILERS = [
    ('text/x-sass', 'django_libsass.SassCompiler'),
    ('text/x-scss', 'django_libsass.SassCompiler'),
]

COMPRESS_ENABLED = config('COMPRESS_ENABLED', cast=bool, default=False)

COMPRESS_OFFLINE = config('COMPRESS_OFFLINE', cast=bool, default=False)

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.rCSSMinFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

# E-mail
# https://docs.djangoproject.com/en/1.9/topics/email/

EMAIL_SUBJECT_PREFIX = '[{{ cookiecutter.project_name }}] '

# Auth
# https://docs.djangoproject.com/en/1.9/topics/auth

LOGIN_REDIRECT_URL = '/'


# Logging
# https://docs.djangoproject.com/en/1.9/topics/logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Testing
# https://model-mommy.readthedocs.io/en/latest/index.html

MOMMY_CUSTOM_FIELDS_GEN = {
    'autoslug.fields.AutoSlugField': 'model_mommy.generators.gen_text',
}

# Messages
# https://docs.djangoproject.com/en/1.9/ref/contrib/messages/

from django.contrib.messages import constants as messages  # NOQA

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
