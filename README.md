# Django CBTP e-mail #

[![Travis CI Badge](https://api.travis-ci.org/illagrenan/django-cbtp-email.png)](https://travis-ci.org/illagrenan/django-cbtp-email)
&nbsp;
[![Coverage Status](https://coveralls.io/repos/illagrenan/django-cbtp-email/badge.svg?branch=master&service=github)](https://coveralls.io/github/illagrenan/django-cbtp-email?branch=master)
&nbsp;
[![Requirements Status](https://requires.io/github/illagrenan/django-cbtp-email/requirements.svg?branch=master)](https://requires.io/github/illagrenan/django-cbtp-email/requirements/?branch=master)

```bash
CBTP
│ │└──Premailer (CSSs ares inlined)
│ └───Template
└─────Class-based (optional)
```

## Installation ##

**This package is not yet on PyPI. Download it from Github:**

```bash
pip install --upgrade git+git://github.com/illagrenan/django-cbtp-email.git#egg=django-cbtp-email
```


**Add `django_cbtp_email` to `INSTALLED_APPS`:**
```python
INSTALLED_APPS = (
    'django_cbtp_email',
)
```

## Usage ##

Create custom mailer (e.g. in `your_app/mailers.py`):

```python
from django_cbtp_email.mailer import Mailer

class TestMailer(Mailer):
    template = "test_mail" # .html is added by default
    subject = "Subject of test mail"
    to = "nobody@localhost"

test_mailer = TestMailer()
test_mailer.send_message()
```

Create e-mail template (e.g. in `your_app/templates/mail/test_email.html`):

```css+django
{% extends "email_base.html" %}

{% block content %}
    <h1>Hello world</h1>

    <p class="first">
        Lorem ipsum...
    </p>

    <footer>
        &copy; 2015 ACME
    </footer>
{% endblock %}
```

Content of `email_base.html`:

```css+django
{% load mailing_tags %}

<!doctype html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Test mail</title>

    <style>
		/* This will be inlined */
        h1 {
            color: red;
        }
    </style>

    {# This will be also inlined #}
	{% css_direct "css/my_css.css" %}
</head>
<body>
{% block content %}{% endblock %}
</body>
</html>
```

You can specify type of rendered template by:

```python
DEFAULT_TEMPLATE_TYPE = "html" # or "txt"
```

