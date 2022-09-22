#from __future__ import print_function
import time
from os import system
from activity import *
import json
import datetime
import sys

if sys.platform in ['Windows', 'win32', 'cygwin']:
    import win_tools as pfm  # pfm stands from platform
elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    import mac_tools as pfm  # pfm stands from platform
elif sys.platform in ['linux', 'linux2']:
    import linux_tools as pfm  # pfm stands from platform

def url_to_name(url):
    string_list = url.split('/')
    return url #string_list[2]


active_window_name = ""
activity_name = ""
activityList = AcitivyList([])
first_time = True
prev_window = None

try:
    activityList.initialize_me()
except Exception:
    print('No json')

try:
    while True:
        curr_window = pfm.get_active_window()
        #if 'Google Chrome' in new_window_name:
        #   new_window_name = url_to_name(pfm.get_chrome_url())

        if curr_window != prev_window:
            print(curr_window)
            #activity_name = curr_window.text
            pfm.inspect_window(curr_window)

            #if not first_time:
            activityList.process_activity(curr_window.text)

            first_time = False
            prev_window = curr_window

        time.sleep(1.5)
    
except KeyboardInterrupt:
    with open('activities.json', 'w') as json_file:
        json.dump(activityList.serialize(), json_file, indent=4, sort_keys=True)
