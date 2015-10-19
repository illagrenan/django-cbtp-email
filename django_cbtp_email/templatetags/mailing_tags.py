# -*- encoding: utf-8 -*-
# ! python2

"""
Template tags.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.template import Library
from django.contrib.staticfiles import finders

from django_cbtp_email.errors import CssForEmailNotFoundError

register = Library()


@register.simple_tag()
def css_direct(css_path):
    """
    :type css_path: str
    """
    if not css_path.endswith(".css"):
        raise ValueError("c")

    result = finders.find(css_path)

    if not result:
        raise CssForEmailNotFoundError(
            "Cannot find \"{}\", searched locations: {}".format(css_path, finders.searched_locations))

    with open(result) as the_file:
        css_content = the_file.read()

    return "<style type=\"text/css\">{0}</style>".format(css_content)
