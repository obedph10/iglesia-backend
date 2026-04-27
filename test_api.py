import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.test import Client
c = Client(SERVER_NAME='localhost')
try:
    response = c.get('/api/contact/settings/')
    print("Status:", response.status_code)
    print("Content:", response.content.decode('utf-8'))
except Exception as e:
    import traceback
    traceback.print_exc()
