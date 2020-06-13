from time import sleep
from win32 import win32gui, win32api


def click(pos):
    x, y = pos
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(2, x, y, 0, 0)
    win32api.mouse_event(4, x, y, 0, 0)
