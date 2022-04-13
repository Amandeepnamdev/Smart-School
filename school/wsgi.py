"""
WSGI config for school project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')
django.setup()
application = get_wsgi_application()
