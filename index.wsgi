import sys
import os.path
import sae
from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'fslss.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'fslss'))


application = sae.create_wsgi_app(WSGIHandler())