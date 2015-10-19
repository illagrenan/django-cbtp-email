# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import logging
import os

from annoying.functions import get_config
from django.conf import settings
from django.template import loader
from django.template import Context
from django.core.mail import EmailMessage
from django.utils import translation
from premailer import Premailer

logger = logging.getLogger(__name__)


def send_mail(subject, template, context, to, from_email=settings.DEFAULT_FROM_EMAIL,
              template_variant=get_config('DEFAULT_TEMPLATE_VARIANT', 'html'), attachment=None):
    """
    Vyrenderuje předanou šablonu do stringu. Dle globálního nastavení nebo předaného posledního parametru se rozhodne,
    zda odešle html nebo txt verzi e-mailu.

    Usage:
        > ctx = { 'some_var': True }
        > send_mail('E-mail subject', 'default_file_extensiontension/emails/bar', context=ctx, to=['joh.doe@example.com'])

    :param template - ceska k šablonám bez koncovky (ta je určena posledním parametrem)
    :param template_variant - txt nebo html (viz nastavení)
    """
    template_path = os.path.normcase('%s.%s' % (template, template_variant))
    # message = render_to_string(template_path, context)

    # context['EMAIL_STATIC_SOURCES_BASE_URL'] = settings.EMAIL_STATIC_SOURCES_BASE_URL
    # context['SITE_URL'] = settings.SITE_URL
    # context['DATE_FORMAT'] = settings.DATE_FORMAT
    # context['DATETIME_FORMAT'] = settings.DATETIME_FORMAT

    context_instance = Context(context)

    current_language = translation.get_language()

    try:
        translation.activate("cs")
        html_message = loader.get_template(template_path).render(context_instance)
    finally:
        translation.activate(current_language)

    premailer = Premailer(
        html_message,
        base_url=get_config('BASE_URL_FOR_EMAIL_LINK', None),
        base_path=settings.STATIC_ROOT
    )

    html_message = premailer.transform()

    mail = EmailMessage(settings.EMAIL_SUBJECT_PREFIX + subject, html_message, to=to, from_email=from_email)
    mail.content_subtype = "html"

    if attachment and os.path.isfile(attachment):
        mail.attach_file(attachment)

    mail.send()


def send_mail_async(*args, **kwargs):
    """
    Asynchronně odešle e-mail.

    :param args:
    :param kwargs:
    """
    send_mail(*args, **kwargs)
