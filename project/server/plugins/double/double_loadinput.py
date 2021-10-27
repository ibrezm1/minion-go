from project.server.plugin_collection import Plugin

class DoubleLoad(Plugin):
    """This plugin will just multiply the argument with the value 2
    """
    def __init__(self,input_data):
        super().__init__(input_data)
        self.load_input({'a':'4'})
        self.description = 'loaded function'
        self.print_vars()


    def perform_operation(self, argument):
        """The actual implementation of this plugin is to multiple the
        value of the supplied argument by 2
        """
        return argument*2
