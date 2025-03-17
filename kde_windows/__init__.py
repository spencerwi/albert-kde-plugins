import subprocess
from albert import *

import dbus

md_iid = '2.4'
md_version = '1.0'
md_name = 'KDE Windows'
md_description = 'Allows you to search windows in KDE (both X11 and Wayland) using kdotool'

__py_deps__ = ["dbus"]

class Plugin(PluginInstance, TriggerQueryHandler):
    def __init__(self):
        PluginInstance.__init__(self)
        TriggerQueryHandler.__init__(self, self.id, self.name, self.description, defaultTrigger = 'w ')

    def handleTriggerQuery(self, query):
        items = []
        query_string = query.string
        list_window_ids_proc = subprocess.run(['kdotool', 'search', query_string], stdout=subprocess.PIPE)
        window_ids = [w.strip() for w in list_window_ids_proc.stdout.decode('utf-8').strip().split('\n') if w.strip()]
        for window_id in window_ids:
            get_window_name_proc = subprocess.run(['kdotool', 'getwindowname', window_id], stdout=subprocess.PIPE)
            window_name = get_window_name_proc.stdout.decode('utf-8').strip()
            get_class_name_proc = subprocess.run(['kdotool', 'getwindowclassname', window_id], stdout=subprocess.PIPE)
            window_class_name = get_class_name_proc.stdout.decode('utf-8').strip()
            if window_name:
                items.append(
                    StandardItem(
                        id=window_id,
                        text=window_name,
                        subtext=window_class_name,
                        iconUrls=['xdg:' + window_class_name],
                        actions=[
                            Action(
                                'activate', 
                                'Activate', 
                                lambda wid=window_id: runDetachedProcess(['kdotool', 'windowactivate', wid]) 
                            )
                        ]
                    )
                 )
        query.add(items)


