import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estacionamento_inteligente.settings')

application = get_wsgi_application()
