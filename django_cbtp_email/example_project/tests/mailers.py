# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
from django_cbtp_email.mailer import Mailer


class TestMailer(Mailer):
    template = "test_mail"
    subject = "Subject of test mail"
    to = "nobody@localhost"