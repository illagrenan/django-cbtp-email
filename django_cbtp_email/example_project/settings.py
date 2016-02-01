# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os

DEBUG = True
ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'Europe/Prague'

LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
)

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
SECRET_KEY = '42'

# EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_FILE_PATH = os.path.join(os.path.dirname(__file__), 'tmp')
