import os
import time

from celery import Celery
from celery.exceptions import Ignore
from celery import states
from celery.utils.log import get_task_logger
import traceback

LOGGER = get_task_logger(__name__)

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="create_bound_task",bind=True)
def create_bound_task(self,task_type):
    print("Calling bound")
    LOGGER.info("stdout: %s" % 'Cat')
    n = 30
    for i in range(0, n):
        self.update_state(state='PROGRESS', meta={'done': i, 'total': n})
        print("Calling bound loop")
        time.sleep(1)
    return n

#https://www.distributedpython.com/2018/09/28/celery-task-states/
@celery.task(name="fail_bound_task",bind=True)
def fail_bound_task(self,task_type):
    try:
        raise ValueError('Some error')
    except Exception as ex:
        self.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': type(ex).__name__,
                'exc_message': traceback.format_exc().split('\n'),
                'custom': '...'
            })
        raise Ignore()
