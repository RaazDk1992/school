import sys
import os
from django.core.wsgi import get_wsgi_application

# Set UTF-8 encoding for output
sys.stdout.reconfigure(encoding="utf-8")
sys.stdin.reconfigure(encoding="utf-8")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolproject.settings')

application = get_wsgi_application()
