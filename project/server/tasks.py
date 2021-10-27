"""Main applicatoin that demonstrates the functionality of
the dynamic plugins and the PluginCollection class
"""

from .plugin_collection import PluginCollection
import inspect

import os
import time

from celery import Celery
from celery.exceptions import Ignore
from celery import states
from celery.utils.log import get_task_logger
from celery.exceptions import SoftTimeLimitExceeded
import traceback

#https://medium.com/@taylorhughes/three-quick-tips-from-two-years-with-celery-c05ff9d7f9eb

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

@celery.task(name="create_bound_plugin",bind=True)
def create_bound_plugin(self,task_type):
    print("Calling bound plugin")
    LOGGER.info("stdout: %s" % 'Cat')
    my_plugins = PluginCollection('project.server.plugins')
    # TODO : Create single return check and raise error if needed
    matching_cls = my_plugins.filter_plugin('loaded')[0]
    try :
        for i in range(0, task_type):
            self.update_state(state='PROGRESS', meta={'done': i, 'total': task_type})
            print("Calling bound loop")
            time.sleep(1)
        return matching_cls.perform_operation(5)
    except SoftTimeLimitExceeded:
        print('Timeout for execution if you want to cleanup')
        pass

def main():
    """main function that runs the application
    """
    my_plugins = PluginCollection('plugins')
    my_plugins.apply_all_plugins_on_value(5)
    matching_cls = my_plugins.filter_plugin('loaded')
    for cl in matching_cls:
        print (f'Applying operation on {cl.description} in {inspect.getfile(cl.__class__)} gives {cl.perform_operation(5)}')

if __name__ == '__main__':
    main()