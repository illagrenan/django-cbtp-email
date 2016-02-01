# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

from django_cbtp_email.mailer import Mailer


class TestMailer(Mailer):
    template = "test_mail"
    subject = "Subject of test mail"
    to = "nobody@localhost"
