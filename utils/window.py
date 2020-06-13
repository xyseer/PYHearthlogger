from win32 import win32gui, win32api, win32process
import os
import signal
import subprocess
from time import sleep
from utils import keyboard
from variables import *
import mss


def get_window_hwnd_by_name(window_name):
    return win32gui.FindWindow(None, window_name)


def move_window_by_hwnd(hwnd, pos):
    win32gui.MoveWindow(hwnd, *pos, True)
    sleep(2)


def close_window_by_name(name):
    try:
        target_hwnd = win32gui.FindWindow(None, name)
        tid, pid = win32process.GetWindowThreadProcessId(target_hwnd)
        os.kill(pid, signal.SIGTERM)
    except:
        pass


def open_window_by_path(path, delay):
    subprocess.Popen(path)
    sleep(delay)


def input_to_cursor(string, cursor_pos):
    keyboard.delete(cursor_pos)
    sleep(1)
    keyboard.input_string(string)
    sleep(1)
    keyboard.press('tab')


def foreground_window_by_hwnd(hwnd):
    win32gui.SetForegroundWindow(hwnd)


def is_all_windows_exist():
    monitor_names = [BUDDY_WINDOW_NAME, GAME_WINDOW_NAME]
    all_name = monitor_names+[CLIENT_LOGIN_WINDOW_NAME, CLIENT_WINDOW_NAME]
    hwnds = []
    for n in monitor_names:
        h = get_window_hwnd_by_name(n)
        hwnds.append(h)
    if 0 in hwnds:
        return False
    return True


def close_all_windows():
    targets = [BUDDY_WINDOW_NAME, GAME_WINDOW_NAME,
               CLIENT_LOGIN_WINDOW_NAME, CLIENT_WINDOW_NAME]
    for t in targets:
        close_window_by_name(t)
        sleep(1)


def get_screenshot(x=0, y=0, width=10, height=10, filename="new_shortcut.png"):
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": y, "left": x,
                   "width": width, "height": height}

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)
