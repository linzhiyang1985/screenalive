import time
import random
import win32api
import win32con

SCREEN_WIDTH = win32api.GetSystemMetrics(0) - 1
SCREEN_HEIGHT = win32api.GetSystemMetrics(1) - 1
INTERVAL = 30 # seconds

def move_mouse(target_position:tuple, steps=40):
    current_x, current_y = win32api.GetCursorPos()
    target_x, target_y = target_position
    x_delta = (target_x - current_x)//steps
    y_delta = (target_y - current_y)//steps
    speed = 3.0 / steps

    for _ in range(steps):
        current_x += x_delta
        current_y += y_delta
        try:
            win32api.SetCursorPos((current_x, current_y))
        except BaseException as ex:
            pass
        time.sleep(speed)

def press_keys(keys=[win32con.VK_LMENU, win32con.VK_TAB]):
    #key down
    for key in keys:
        win32api.keybd_event(key, 0, 0, 0)
    #key up
    for key in keys:
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

if __name__ == '__main__':
    while True:
        try:
            action = random.choice([0,1])
            if action == 0:
                press_keys()
                time.sleep(1)
                press_keys()
            elif action == 1:
                move_mouse(
                    (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
                )
        except BaseException:
            pass
        #interval
        time.sleep(INTERVAL)