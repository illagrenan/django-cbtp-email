# coding=utf-8

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import sys

import six

if not six.PY2:
    print("Run Fabfile only under Python 2.x")
    sys.exit(0)

from fabric.context_managers import settings

from fabric.contrib.console import confirm
from fabric.decorators import task
from fabric.operations import local


@task()
def test_install():
    with settings(warn_only=True):
        local("pip uninstall django_cbtp_email --yes")
        print("Uninstall OK.")

    local("pip install --use-wheel --no-index --find-links dist django_cbtp_email")
    local("pip uninstall django_cbtp_email --yes")

    print("Install OK.")


@task()
def test():
    local("nosetests --with-coverage --cover-package=django_cbtp_email "
          "--cover-tests --cover-erase --with-doctest --nocapture")

    # local("py.test django_cbtp_email -s --doctest-modules --cov=django_cbtp_email")

    print("Test OK.")


@task()
def build():
    local("python setup.py sdist")
    local("python setup.py bdist_wheel")

    print("Build OK.")


@task()
def publish():
    if confirm(u'Really publish?', default=False):
        local('python setup.py sdist upload -r pypi')
        local('python setup.py bdist_wheel upload -r pypi')

        print("Published.")
