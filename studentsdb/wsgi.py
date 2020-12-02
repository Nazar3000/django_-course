"""
WSGI config for studentsdb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentsdb.settings")

from django.core.wsgi import get_wsgi_application
=======
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentsdb.settings")

>>>>>>> e336e2e04061f1c7141d0980d2e41951f3af73af
application = get_wsgi_application()
