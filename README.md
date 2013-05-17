==================
django-userattritutes
==================

[![Build Status](https://travis-ci.org/cschwede/django-userattributes.png?branch=master)](https://travis-ci.org/cschwede/django-userattritutes)

Extend Django UserAdmin with flexible user attributes and one or more filters to UserAdmin.

Quick start
-----------

1. Add "userattributes" to your INSTALLED_APPS setting like this:

````python
INSTALLED_APPS = (
    ...
    'userattributes',
)
```

2. Run `python manage.py syncdb` to create the models

3. Set USERATTRIBUTE_FILTER_COUNT to the number of filters

4. Extend your admin.py:

````python
from django.contrib import admin
from userattributes.admin import UserAdminWithAttributes

admin.site.unregister(User)
admin.site.register(User, UserAdminWithAttributes)
```

5. Start the development server and visit http://127.0.0.1:8000/admin/
