import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_channels_tutorials.settings')
app = Celery('django_channels_tutorials')
app.config_from_object('django.conf:settings', namespace='CELERY')

# 设定定时任务
app.conf.beat_schedule = {
    'get_joke_5s': {
        'task': 'jokes.tasks.get_joke',
        'schedule': 5.0
    }
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
