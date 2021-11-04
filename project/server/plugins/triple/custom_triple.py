from project.server.plugin_collection import Plugin
from celery import Celery, states
import traceback
import time
import os.path
import inspect
import json
from pathlib import Path

class CustomLoad(Plugin):
    """This plugin will just multiply the argument with the value 2
    """
    def __init__(self,input_data):
        super().__init__(input_data)
        self.load_input({'a':'4'})
        self.description = 'Custom triple function'
        self.print_vars()

    def loadfile(self):
        pathf = Path(inspect.getfile(self.__class__))
        loadpath = os.path.join(pathf.parent,'loadinput.json')
        print(f'Load path {type(loadpath)} and val {loadpath}')
        with open(loadpath) as f:
            data = json.load(f)
        self.load_input(data)

    def perform_operation2(self, celery, kwargs):
        self.loadfile()
        self.print_vars()
        """The actual implementation of this plugin is to multiple the
        value of the supplied argument by 2
        """
        print(f'kwargs : {kwargs}')
        celery.update_state(state='PROGRESS', meta={'done': 'i', 'total': 'task_type'})
        time.sleep(int(kwargs['time']))
        return 6

    def soft_timeout(self, celery, kwargs):
        """The actual implementation of this plugin is to multiple the
        value of the supplied argument by 2
        """
        print(f'kwargs : {kwargs}')
        print('Soft timed out')
        celery.update_state(
            state=states.FAILURE,
            meta={
                'exc_type': 'Some Reason',
                'exc_message': traceback.format_exc().split('\n'),
                'custom': '...'
            })
        raise ValueError('Soft timeout Exceeded')
        return -1