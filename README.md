# django_cbtp_email #

[![Travis CI Badge](https://api.travis-ci.org/illagrenan/django-custom-500.png)](https://travis-ci.org/illagrenan/django-custom-500)
&nbsp;
[![Coverage Status](https://coveralls.io/repos/illagrenan/django-custom-500/badge.svg?branch=master)](https://coveralls.io/r/illagrenan/django-custom-500?branch=master)
&nbsp;
[![Requirements Status](https://requires.io/github/illagrenan/django-custom-500/requirements.svg?branch=master)](https://requires.io/github/illagrenan/django-custom-500/requirements/?branch=master)

## Installation ##

**This package is not yet on PyPI. Download it from Github:**

```bash
pip install --upgrade git+git://github.com/illagrenan/django-custom-500.git#egg=django-custom-500
```


**Add `django_custom_500` to `INSTALLED_APPS`:**
```python
INSTALLED_APPS = (
    'django_custom_500',
)
```

## Usage ##

Create `500.html` in your `template` folder.

**OR**

Set `CUSTOM_500_TEMPLATE` in your settings.

Example:

```python
CUSTOM_500_TEMPLATE = "my/path/to/500.html"
```