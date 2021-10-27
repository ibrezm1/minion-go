"""Main applicatoin that demonstrates the functionality of
the dynamic plugins and the PluginCollection class
"""

from plugin_collection import PluginCollection
import inspect

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
