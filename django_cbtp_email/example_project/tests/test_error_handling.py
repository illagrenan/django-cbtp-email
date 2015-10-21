# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.template import TemplateDoesNotExist
from django.test import TestCase, override_settings

from ..tests.mailers import TestMailer


class ErrorHandlingTestCase(TestCase):
    @override_settings(DEBUG=True)
    def test_cannot_send_email_with_invalid_template(self):
        test_mailer = TestMailer()
        test_mailer.template = "dummy_template"

        # Wrong template
        self.assertRaises(TemplateDoesNotExist, test_mailer.send_message)

    def test_invalid_template_cannot_be_attached(self):
        test_mailer = TestMailer()

        # Wrong template
        self.assertRaises(ValueError, test_mailer.attach_file, file_path="dummy_file")
