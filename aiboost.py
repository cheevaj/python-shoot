from pyautogui import *
import time
import keyboard
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Get the screen arrangement dimensions
screen_width, screen_height = size()

# Padding
padding = 100

# Calculate new region
region_left = padding
region_top = padding
region_width = screen_width - 2*padding
region_height = screen_height - 2*padding

while keyboard.is_pressed('q') == False:
    flag = 0
    pic = screenshot(region=(region_left, region_top, region_width, region_height))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r, g, b = pic.getpixel((x, y))

            if b == 195 and r == 255 and g == 219:
                flag = 1
                click(x + region_left, y + region_top)
                time.sleep(0.02)
                break

        if flag == 1:
            break
