from project.server.plugin_collection import Plugin
import time

class CustomLoad(Plugin):
    """This plugin will just multiply the argument with the value 2
    """
    def __init__(self,input_data):
        super().__init__(input_data)
        self.load_input({'a':'4'})
        self.description = 'CustomLoad loaded function'
        self.print_vars()


    def perform_operation2(self, celery, kwargs):
        """The actual implementation of this plugin is to multiple the
        value of the supplied argument by 2
        """
        print(f'kwargs : {kwargs}')
        celery.update_state(state='PROGRESS', meta={'done': 'i', 'total': 'task_type'})
        return 2
