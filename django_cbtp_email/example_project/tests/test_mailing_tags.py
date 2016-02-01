# -*- encoding: utf-8 -*-
# ! python2

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os

import mock as mock
from django.template import Context, Template
from django.test import TestCase

from ...errors import CssForEmailNotFoundError
from ...templatetags.mailing_tags import static_direct


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


class ATemplateTagsTestCase(TestCase):
    @mock.patch('django.template.Context')
    def test_absolute_path(self, context):
        rendered_tpl_string = Template(
            "{% load mailing_tags %}"
            "{% static_direct \"css/my_css.css\" %}"
        ).render(Context({}))
        """:type : str """

        # TODO Assert with regex
        self.assertIn("file:///", rendered_tpl_string)
        self.assertIn("my_css.css", rendered_tpl_string)

    @mock.patch('django.template.Context')
    def test_absolute_path_exists(self, context):
        file_path = static_direct(context, "css/my_css.css")
        """:type : str """

        self.assertTrue(os.path.isfile(file_path.replace("file:///", "")))

    @mock.patch('django.template.Context')
    def test_with_request_no_absolute_path(self, context):
        rendered_tpl_string = Template(
            "{% load mailing_tags %}"
            "{% static_direct \"css/my_css.css\" %}"
        ).render(Context({'request': True}))
        """:type : str """

        # TODO Assert with regex
        self.assertNotIn("file:///", rendered_tpl_string)
        self.assertIn("my_css.css", rendered_tpl_string)
