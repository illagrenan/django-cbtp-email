# -*- encoding: utf-8 -*-
# ! python2

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.template import Context, Template
from django.test import TestCase
import mock as mock

from ...errors import CssForEmailNotFoundError


class MailingTemplateTagsTestCase(TestCase):
    @mock.patch('django.template.Context')
    def test_css_file_is_read_and_included(self, context):
        rendered_tpl_string = Template(
            "{% load mailing_tags %}"
            "{% css_direct \"css/my_css.css\" %}"
        ).render(Context({}))
        """:type : str """

        self.assertIn("font-size: 42pt;", rendered_tpl_string)

    @mock.patch('django.template.Context')
    def test_not_found_error_on_invalid_file(self, context):
        tpl_to_render = Template(
            "{% load mailing_tags %}"
            "{% css_direct \"css/this_file_doesnt_exist.css\" %}"
        )

        self.assertRaises(CssForEmailNotFoundError, tpl_to_render.render, Context({}))

    @mock.patch('django.template.Context')
    def test_fail_to_load_non_css_file(self, context):
        tpl_to_render = Template(
            "{% load mailing_tags %}"
            "{% css_direct \"css/my_css.PNG\" %}"
        )

        self.assertRaises(ValueError, tpl_to_render.render, Context({}))
