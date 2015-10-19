# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import
import os
import tempfile

from django.test import TestCase

from ..tests.mailers import TestMailer


class BasicUsageTestCase(TestCase):
    def test_message_will_be_sent_with_inlined_css(self):
        test_mailer = TestMailer()
        test_mailer.send_message()

        from django.core.mail import outbox

        assert len(outbox) == 1

        sent_message = outbox[0]
        """:type : django.core.mail.EmailMessage """

        assert TestMailer.subject in sent_message.subject
        assert TestMailer.to in sent_message.to
        assert "<p style=\"font-size:42pt\">" in sent_message.body

    def test_attachment(self):
        test_mailer = TestMailer()

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp:
            test_mailer.attach_file(temp.name)
            test_mailer.send_message()

        from django.core.mail import outbox

        assert len(outbox) == 1

        os.remove(temp.name)

    def test_empty_recipient(self):
        test_mailer = TestMailer(to=None)

        # Recipient is not set
        self.assertRaises(ValueError, test_mailer.send_message)
