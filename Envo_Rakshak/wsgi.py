"""
WSGI config for Envo_Rakshak project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise # type: ignore

from Envo_Rakshak import MyWSGIApp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Envo_Rakshak.settings')

application = get_wsgi_application()

app = application

application = MyWSGIApp()
application = WhiteNoise(application, root="static/")