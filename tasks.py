# -*- encoding: utf-8 -*-
# ! python3

import shutil

from invoke import run, task

PROJECT_NAME = 'django_cbtp_email'


@task
def clean():
    """remove build artifacts"""
    shutil.rmtree('{PROJECT_NAME}.egg-info'.format(PROJECT_NAME=PROJECT_NAME), ignore_errors=True)
    shutil.rmtree('build', ignore_errors=True)
    shutil.rmtree('dist', ignore_errors=True)
    shutil.rmtree('htmlcov', ignore_errors=True)
    shutil.rmtree('__pycache__', ignore_errors=True)


@task
def lint():
    """check style with flake8"""
    run("flake8 {PROJECT_NAME}/ tests/".format(PROJECT_NAME=PROJECT_NAME))


@task
def test():
    run("nosetests -v --with-coverage --cover-package=django_cbtp_email --cover-tests --cover-erase --with-doctest --nocapture")


@task
def test_all():
    """run tests on every Python version with tox"""
    run("tox")


@task
def check():
    """Check setup"""
    run("python setup.py --no-user-cfg --verbose check --metadata --restructuredtext --strict")


@task
def test_install():
    """try to install built package"""
    run("pip uninstall {PROJECT_NAME} --yes".format(PROJECT_NAME=PROJECT_NAME), warn=True)
    run("pip install --use-wheel --no-cache-dir --no-index --find-links=file:./dist {PROJECT_NAME}".format(PROJECT_NAME=PROJECT_NAME))
    run("pip uninstall {PROJECT_NAME} --yes".format(PROJECT_NAME=PROJECT_NAME))


@task
def build():
    """build package"""
    run("python setup.py build")
    run("python setup.py sdist")
    run("python setup.py bdist_wheel")


@task
def publish():
    """publish package"""
    check()
    run('python setup.py sdist upload -r pypi')  # Use python setup.py REGISTER
    run('python setup.py bdist_wheel upload -r pypi')


@task
def publish_twine():
    """publish package"""
    check()
    run('twine upload dist/* --skip-existing')


@task
def publish_test():
    """publish package"""
    check()
    run('python setup.py sdist upload -r https://testpypi.python.org/pypi')  # Use python setup.py REGISTER
    run('python setup.py bdist_wheel upload -r https://testpypi.python.org/pypi')
