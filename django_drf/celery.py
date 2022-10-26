import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_drf.settings')

app = Celery('django_drf',
             broker='redis://localhost:14000/0', backend="redis://localhost:14000/1"
             )

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(name='Add two numbers')
def add(x, y):
    return x + y