from win32 import win32gui, win32api, win32event
from utils import mouse
from utils.virtual_key import *
from time import sleep


def press(key):
    if key.isalpha():
        key = key.lower()
    if key == '@':
        win32api.keybd_event(keys['shift'], 0, 0, 0)
        win32api.keybd_event(keys['2'], 0, 0, 0)
        win32api.keybd_event(keys['2'], 0, 2, 0)
        win32api.keybd_event(keys['shift'], 0, 2, 0)
    else:
        win32api.keybd_event(keys[key], 0, 0, 0)
        win32api.keybd_event(keys[key], 0, 2, 0)


def delete(pos):
    mouse.click(pos)
    mouse.click(pos)
    mouse.click(pos)
    sleep(1)
    press("del")


def input_string(string):
    for key in string:
        press(key)
        sleep(0.1)

def ctrlshiftaltv():
    win32api.keybd_event(keys['shift'], 0, 0, 0)
    win32api.keybd_event(keys['ctrl'], 0, 0, 0)
    win32api.keybd_event(keys['alt'], 0, 0, 0)
    win32api.keybd_event(keys['v'],0, 0, 0)
    win32api.keybd_event(keys['v'], 0, 2, 0)
    win32api.keybd_event(keys['ctrl'], 0, 2, 0)
    win32api.keybd_event(keys['alt'], 0, 2, 0)
    win32api.keybd_event(keys['shift'], 0, 2, 0)
    
