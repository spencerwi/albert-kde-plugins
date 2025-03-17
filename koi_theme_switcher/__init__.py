import subprocess
from albert import *

md_iid = '2.4'
md_version = '1.0'
md_name = 'Koi theme switcher'
md_description = 'Switches between dark/light themes using Koi'
md_lib_dependencies = ['dbus-python']

__py_deps__ = ["dbus-python"]

import dbus

class ThemeSwitcherController():
    def __init__(self):
        self.session_bus = dbus.SessionBus()

    def invoke_koi(self, method_name):
        service_name = "dev.baduhai.Koi"
        object_path = "/Koi"
        interface_name = 'local.KoiDbusInterface'
        proxy_object = self.session_bus.get_object(service_name, object_path)
        method = proxy_object.get_dbus_method(method_name, dbus_interface=interface_name)
        method()
         
    def light_mode(self): 
        self.invoke_koi('goLightMode')

    def dark_mode(self): 
        self.invoke_koi('goDarkMode')

    def toggle(self): 
        self.invoke_koi('toggleMode')

class Plugin(PluginInstance, TriggerQueryHandler):
    def __init__(self):
        PluginInstance.__init__(self)
        TriggerQueryHandler.__init__(self, id='koi_theme_switcher', name=md_name, description=md_description, defaultTrigger='koi ')
        self.controller = ThemeSwitcherController()

    def handleTriggerQuery(self, query):
        items = []
        if not query.string or query.string.lower() in "light":
            items.append(
                StandardItem(
                    id = self.id + "-lightmode",
                    iconUrls=["xdg:flashlight-on"],
                    text = 'Koi: Light mode',
                    actions = [Action('koi lightmode', 'Koi: Light mode', lambda ctl=self.controller: ctl.light_mode())]
                )
            )
        if not query.string or query.string.lower() in "dark":
            items.append(
                StandardItem(
                    id = self.id + "-darkmode",
                    iconUrls=["xdg:flashlight-off"],
                    text = 'Koi: Dark mode',
                    actions = [Action('koi darkmode', 'Koi: Dark mode', lambda ctl=self.controller: ctl.dark_mode())]
                )
            )
        if not query.string or query.string.lower() in "toggle":
            items.append(
                StandardItem(
                    id = self.id + "-togglemode",
                    iconUrls=["xdg:koi_tray"],
                    text = 'Koi: Toggle mode',
                    actions = [Action('koi toggle', 'Koi: Toggle mode', lambda ctl=self.controller: ctl.toggle())]
                )
            )
        if items:
            query.add(items)


