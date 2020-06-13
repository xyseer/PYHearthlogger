from utils import keyboard, window, mouse, tools
from variables import *
from time import sleep
import subprocess
from pyaudio import *

import wave


def play():
    chunk=1024  #2014kb
    wf=wave.open(r"error.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=wf.getnchannels(),rate=wf.getframerate(),output=True)
 
    data = wf.readframes(chunk)  # 读取数据
    #print(data)
    while data !=b'':  # 播放  必须用b''停
        stream.write(data)
        data = wf.readframes(chunk)
        #print('while循环中！')
        #print(data)
    #print('breakpoint！')
    stream.stop_stream()   # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio

def pyhl_starter():
    global dfu
    window.open_window_by_path('./main.exe',5)
    #print("起")
    PYHL_HWND=window.get_window_hwnd_by_name(PYHL_NAME)
    sleep(30)
    if not PYHL_HWND:
        print("can't start PYHearthLogger,now retry")
    else:
        dfu=pyhl_monitor
    return

def pyhl_monitor():
    global dfu,RESTART_STATS
    PYHL_HWND=window.get_window_hwnd_by_name(PYHL_NAME)
    if not PYHL_HWND:
        print("HL DEAD ,now revive it")
        dfu=pyhl_starter
        RESTART_STATS+=1
    else:
        sleep(3600)
    return




dfu=pyhl_monitor
RESTART_STATS=0



try:
    print("Engine of PYHearthLogger has started")
    while True:
        print("PYHL is running...  restart=",RESTART_STATS)
        dfu()
        #raise ValueError()
except Exception as e:
    print(e)
    print("error,自动退出")
    play()
    sleep(5)
    os._exit(0)
