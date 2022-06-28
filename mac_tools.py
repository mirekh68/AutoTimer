from AppKit import NSWorkspace
    from Foundation import *

def get_active_window():
    _active_window_name = None
    active_window_name = (NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])
    return _active_window_name

def get_chrome_url():
    textOfMyScript = """tell app "google chrome" to get the url of the active tab of window 1"""
    s = NSAppleScript.initWithSource_(
        NSAppleScript.alloc(), textOfMyScript)
    results, err = s.executeAndReturnError_(None)
    return results.stringValue()
