"""
WSGI config for get_details_aadharcard_or_pancard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'get_details_aadharcard_or_pancard.settings')

application = get_wsgi_application()
