"""
The simplest Celery app initialisation
Copy tretiak@gmail.com / https://github.com/xmig
Any restriction for using
"""

import sys
from datetime import timedelta
from celery import Celery
sys.path.append("./")


# Celery
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
class CeleryConnection:
    BROKER_URL = 'redis://localhost:6379/1'
    ASYNC_RESULT_DB = 2
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/{}'.format(str(ASYNC_RESULT_DB))
    CELERY_TIMEZONE = 'UTC',
    # CELERYBEAT_SCHEDULE = {
    #     'periodic_task': {
    #         'task': 'sysutils.async.celery.task.periodic_task_performer',
    #         'schedule': timedelta(seconds=10),
    #         'args': (("sysutils.async.tasks.web.event_task.GetEventTask",))
    #     }
    # }


celery_app = Celery(__name__)
celery_app.config_from_object(CeleryConnection)

