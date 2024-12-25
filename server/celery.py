import os
from celery import Celery
from celery import signals
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

logger = logging.getLogger('celery')

@app.task(bind=True)
def debug_task(self):
    logger.info(f'Request: {self.request!r}')

@signals.setup_logging.connect
def setup_celery_logging(**kwargs):
    from django.conf import settings
    logging.config.dictConfig(settings.LOGGING)

@signals.task_failure.connect
def task_failure_handler(sender=None, task_id=None, exception=None, args=None, kwargs=None, **kwds):
    logger.error(f'Task {sender.name} failed: {exception}')
