from project.server import plugin_collection 

class Identity(plugin_collection.Plugin):
    """This plugin is just the identity function: it returns the argument
    """
    def __init__(self,input_data):
        super().__init__(input_data)
        self.description = 'Identity function'
    



    def perform_operation(self, argument):
        """The actual implementation of the identity plugin is to just return the
        argument
        """
        return argument
