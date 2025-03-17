import subprocess
from albert import *


md_iid = '2.4'
md_version = '1.0'
md_name = 'KDE Night Switch'
md_description = 'Toggles KDE\'s Night Color feature'
md_lib_dependencies = ['dbus-python']

__py_deps__ = ["dbus-python"]

import dbus

class NightColorController():
    def __init__(self):
        self.session_bus = dbus.SessionBus()

    def toggle(self): 
            service_name = "org.kde.kglobalaccel"
            object_path = "/component/kwin"
            interface_name = 'org.kde.kglobalaccel.Component'
            method_name = "invokeShortcut"
            shortcut = "Toggle Night Color"
            proxy_object = self.session_bus.get_object(service_name, object_path)
            interface = dbus.Interface(proxy_object, interface_name)
            interface.invokeShortcut(shortcut)

class Plugin(PluginInstance, TriggerQueryHandler):
    def __init__(self):
        PluginInstance.__init__(self)
        TriggerQueryHandler.__init__(self, id='kde_night_switch', name=md_name, description=md_description, defaultTrigger='kns')
        self.controller = NightColorController()

    def defaultTrigger(self):
        return 'kns '

    def handleTriggerQuery(self, query):
        item = StandardItem(
            id = self.id,
            iconUrls=["xdg:redshift-status-on"],
            text = 'Toggle Night Color',
            actions = [Action('Toggle Night Color', 'Toggle Night Color', lambda ctl=self.controller: ctl.toggle())]
        )
        query.add(item)


