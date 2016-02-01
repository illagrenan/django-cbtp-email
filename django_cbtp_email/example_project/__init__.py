# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys

if "nosetests" in sys.argv[0]:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_cbtp_email.example_project.settings")

    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()
