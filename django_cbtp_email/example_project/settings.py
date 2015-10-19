# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import os

DEBUG = False
ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'Europe/Prague'

LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django_cbtp_email',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages'
)

ROOT_URLCONF = 'django_cbtp_email.example_project.urls'
SECRET_KEY = 'any-key'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'  # change this to a proper location
