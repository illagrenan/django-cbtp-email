# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.test import TestCase


class DummyTestCase(TestCase):
    def test_will_always_pass(self):
        self.assertTrue(True)
