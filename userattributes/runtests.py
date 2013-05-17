""" This file mainly exists to allow python setup.py test to work. """

import os
import sys
from django.conf import settings

settings.configure(
    DEBUG=True,
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'testdb',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'userattributes',),
    USERATTRIBUTE_FILTER_COUNT=3
)

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.test.utils import get_runner


def runtests():
    """ Runs test.py """
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['userattributes'])
    sys.exit(bool(failures))

if __name__ == '__main__':
    runtests()
