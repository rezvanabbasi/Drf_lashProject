from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('LashCenter')
app.config_from_object("config.celery", namespace='CELERY')
app.autodiscover_tasks()

app.conf.update(
    task_routes={
        "tasks.kave_negar_token_send": "q1"
    },
    task_annotations={
        "tasks.kave_negar_token_send": {"rate_limit": "10/m"}
    },
    timezone='UTC',
)
