import win32gui
import uiautomation as auto


# also see here: https://stackoverflow.com/questions/59595763/get-active-chrome-url-in-python

def EnumPropsFunc(hwnd, propname, propdatahandle, win_obj):
    win_obj.props[propname] = propdatahandle
    return True

class Window:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.text = win32gui.GetWindowText(hwnd)
        self.class_name = win32gui.GetClassName(hwnd)
        self.props = {}
        win32gui.EnumPropsEx(hwnd,EnumPropsFunc, self)

        self.children = []

    def __eq__(self, other):
        if type(self) is not type(other):
            return False
        return self.hwnd == other.hwnd and self.text == other.text

    def __neq__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"[{hex(self.hwnd)} : {self.text}]"


def get_active_window():
    _active_window_name = None
    hwnd = win32gui.GetForegroundWindow()
    #name = win32gui.GetWindowText(hwnd)
    return Window(hwnd)

def process_win(hwnd, param):
    #text = win32gui.GetWindowText(hwnd)
    #class_name = win32gui.GetClassName(hwnd)
    #win = Window(hwnd,text)
    parent_window = param[1]
    inspector = param[0]
    win = Window(hwnd)
    parent_window.children.append(win)
    inspector.inspect(win)
    return True

class WinInspector:
    def __init__(self, win):
        self.window = win
        self.children = set()

    def inspect(self, win):
        hwnd = win.hwnd
        if win.hwnd not in self.children:
            print(f"Processing window: hwnd: {hex(hwnd)} ; class: {win.class_name} ; text: {win.text}")
            print(f"Properties: {win.props}")
            self.children.add(hwnd)
            win32gui.EnumChildWindows(hwnd, process_win, (self,win))


def printwin(hwnd, param):
    text = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)
    print(f"{hwnd} : {class_name} : {text}")
    inspect_window(Window(hwnd,text))
    return True

#def get_chrome_url():
def inspect_window(win):
    #window = win32gui.GetForegroundWindow()
    winInspector = WinInspector(win)
    winInspector.inspect(win)


    # chromeControl = auto.ControlFromHandle(window)
    # edit = chromeControl.


    return "Chrome"  # https://' + edit.GetValuePattern().Value
