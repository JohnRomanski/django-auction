#!/usr/bin/env python
"""
This script is a trick to setup a fake Django environment, since this reusable
app will be developed and tested outside any specific Django project.

Via ``settings.configure`` you will be able to set all necessary settings
for your app and run the tests as if you were calling ``./manage.py test``.

"""
import os
import sys

from django.conf import settings

from django.apps import apps
    
EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]
INTERNAL_APPS = [
    'django_nose',
    'auction',
]
INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS

if not settings.configured:
    settings.configure(
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            }
        },
        INSTALLED_APPS=INSTALLED_APPS,
        ROOT_URLCONF='auction.tests.urls',
        TEMPLATE_DIRS=(
            os.path.join(os.path.dirname(__file__), '../templates'),
        ),
        USE_TZ=True,
    )

if not apps.ready and not settings.configured:
    django.setup()

from django_nose import NoseTestSuiteRunner

def runtests(*test_args):
    failures = NoseTestSuiteRunner(verbosity=2, interactive=True).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
