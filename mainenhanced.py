import pywintypes
try:
    from utils import keyboard, window, mouse, tools
    from variables import *
    import threading
    from time import sleep
    import json
    import subprocess
    from tkinter import *
except Exception as e:
    print("发生了导入错误, 请告知楼主（详见importerror.txt）")
    print(e)
    os._exit()
print("insert succeed!now running main steps")
Restart_Stats=0

def windowstart1():
    myWindow = Tk()
    #设置标题
    myWindow.title('HL')
    #设置窗口大小
    width = 100
    height = 100
      
    #获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = myWindow.winfo_screenwidth() 
    screenheight = myWindow.winfo_screenheight()
    myWindow.withdraw()
    myWindow.mainloop()
    
def start_all():
    global dfu, sum, Restart_Stats
    sum = -1
    if (Restart_Stats==0):
        window.open_window_by_path(CLIENT_PATH, CLIENT_DELAY)
        '''login_hwnd = window.get_window_hwnd_by_name(CLIENT_LOGIN_WINDOW_NAME)
        if not login_hwnd:
            print("cant start battle client")
            dfu = monitor
            return
        window.move_window_by_hwnd(login_hwnd, CLIENT_LOGIN_POS)
        window.foreground_window_by_hwnd(login_hwnd)
        # 输入账号密码，登录
        window.input_to_cursor(CURRENT_ACCOUNT, LOGIN_ACCOUT_CLICK_POS)
        window.input_to_cursor(CURRENT_PASSWORD, LOGIN_PASSWORD_CLICK_POS)
        mouse.click(LOGIN_ENTER_CLICK_POS)
        sleep(LOGIN_DELAY)'''
        # 调整窗口大小、位置
        client_hwnd = window.get_window_hwnd_by_name(CLIENT_WINDOW_NAME)
        if not client_hwnd:
            print("cant start battle client")
            dfu = monitor
            return
    client_hwnd = window.get_window_hwnd_by_name(CLIENT_WINDOW_NAME)
    window.move_window_by_hwnd(client_hwnd, CLIENT_POS)
    window.foreground_window_by_hwnd(client_hwnd)

    
    # 启动游戏
    mouse.click(CLIENT_CLICK_POS)
    sleep(GAME_START_DELAY)
    game_hwnd = window.get_window_hwnd_by_name(GAME_WINDOW_NAME)

    if not game_hwnd:
        print("failed starting game, retry now")
        return
    window.move_window_by_hwnd(game_hwnd, GAME_POS)
    # 运行脚本

    def start_buddy():
        ###default start
        hwnd = window.get_window_hwnd_by_name(BUDDY_WINDOW_NAME)
        sleep(3)
        window.move_window_by_hwnd(hwnd, BUDDY_POS)
        win32gui.SetForegroundWindow(hwnd)
        rect = win32gui.GetWindowRect(hwnd)
        # if rect[2] != BUDDY_WIDTH or rect[3] != BUDDY_HEIGHT:
        #     print(
        #         "error, can't change buddy width to {}*{}".format(BUDDY_WIDTH, BUDDY_HEIGHT))
        #     return

        print("trying to click at the start button...")
        sleep(2)
        mouse.click(BUDDY_CLICK_POS)
        print("clicked")
        '''if rect[3] < 900:
            print("cant trigger auto concede, because buddy height is less than 900")
        elif AUTO_CONCEDE_ENABLE:
            print("try to trigger auto_concede_mode")
            mouse.click(CONFIG_POS)
            sleep(1)
            mouse.click(USER_POS)
            sleep(1)
            mouse.click(AUTO_CONCEDE_POS)
            print("auto concede mode should be triggerd")'''

        return
    a = os.listdir(LOGS_PATH)
    subprocess.Popen(BUDDY_PATH)
    print("buddy started, waiting until it's readdy")
    susbended_time = 0
    buddy_started = False
    
#verify part
    print("verufying buddy")
    #hwnd = window.get_window_hwnd_by_name("")
    keyboard.ctrlshiftaltv()
    sleep(10)
    mouse.click(BUDDY_VERIFY_POS)
    sleep(5)
    mouse.click(BUDDY_CONFIRM_POS)
    
#normal start
    while susbended_time <= BUDDY_START_DELAY and (not buddy_started):
        b = os.listdir(LOGS_PATH)
        for f in a:
            b.remove(f)
        if b:
            print("detects log generated, waiting")

            while (not buddy_started)and susbended_time <= BUDDY_START_DELAY:
                new_log = b[0]
                size = os.path.getsize(os.path.join(LOGS_PATH, new_log))
                if size >= 9340:
                    origin_size = size
                    print(
                        "log fully generated, buddy should be ready.\n try to start hearthbuddy")
                    sleep(2)
                    start_buddy()
                    sleep(2)
                    size = os.path.getsize(os.path.join(LOGS_PATH, new_log))
                    if size > origin_size:
                        print("buddy started successfully")
                        buddy_started = True
                else:
                    sleep(3)
                    susbended_time += 3
        else:
            sleep(3)
            susbended_time += 3
    if not buddy_started:
        print("can't start buddy, retry")
    else:
        print("buddy started, switch to monitor mode")
        os.system("cls")
        Restart_Stats += 1
        dfu = monitor


def monitor():
    global sum, dfu
    current_sum = tools.sum_stat()
    if not window.is_all_windows_exist() or sum == current_sum:
        print("error in the whole process. ready to relog")
        window.close_all_windows()
        dfu = start_all
        return
    else:
        sum = current_sum
        sleep(TIME_PER_GAME)


sum = -1
dfu = monitor

try:
    #child = subprocess.Popen("./frame.exe")
    t = threading.Thread(target=windowstart1,name="Thread2")
    t.start()
    while True:
        print("pyhearthlogger still running...")
        print("restart stats is:",Restart_Stats)
        dfu()        
except Exception as e:
    print("发生了错误, 请告知楼主（详见error.txt)")
    with open("error.txt", "a")as f:
        f.write("运行错误: "+str(e))
    from time import sleep
    sleep(5)
    print("自动退出")
    #child.kill()
    os._exit(0)
