import pyautogui
from pyautogui import *
import time
import keyboard
import win32api, win32con
import cv2
import tkinter as tk
import numpy as np

def click(x, y):
    # Function to simulate a mouse click at specified coordinates (x, y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Get the screen arrangement dimensions
screen_width, screen_height = pyautogui.size()
# Padding
padding = 100
# Calculate new region
region_left = padding
region_top = padding
region_width = screen_width - 2 * padding
region_height = screen_height - 2 * padding

image_check1 = cv2.imread('Image/test1.jpg', 0)
image_check2 = cv2.imread('Image/test2.jpg', 0)

def check_and_click():
    # Capture the screenshot of the specified region
    pic = pyautogui.screenshot(region=(region_left, region_top, region_width, region_height))

    # Convert the screenshot to grayscale
    gray_pic = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2GRAY)

    # Use OpenCV template matching to find the first image
    res1 = cv2.matchTemplate(gray_pic, image_check1, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc1 = np.where(res1 >= threshold)

    # Use OpenCV template matching to find the second image
    res2 = cv2.matchTemplate(gray_pic, image_check2, cv2.TM_CCOEFF_NORMED)
    loc2 = np.where(res2 >= threshold)

    # If both images are found, click on both images
    if len(loc1[0]) > 0 and len(loc2[0]) > 0:
        # Click on the middle of the first found bounding box of the first image
        x_center_1 = int(loc1[1][0] + region_left + (image_check1.shape[1] / 2))
        y_center_1 = int(loc1[0][0] + region_top + (image_check1.shape[0] / 2))
        click(x_center_1, y_center_1)

        # Click on the middle of the first found bounding box of the second image
        x_center_2 = int(loc2[1][0] + region_left + (image_check2.shape[1] / 2))
        y_center_2 = int(loc2[0][0] + region_top + (image_check2.shape[0] / 2))
        click(x_center_2, y_center_2)

        time.sleep(0.02)  # Add a small delay for stability
        return True
    elif len(loc1[0]) > 0:
        # Click on the middle of the first found bounding box of the first image
        x_center = int(loc1[1][0] + region_left + (image_check1.shape[1] / 2))
        y_center = int(loc1[0][0] + region_top + (image_check1.shape[0] / 2))
        click(x_center, y_center)  # Perform a mouse click at the center of the found image
        time.sleep(0.02)  # Add a small delay for stability
        return True
    elif len(loc2[0]) > 0:
        # Click on the middle of the first found bounding box of the second image
        x_center = int(loc2[1][0] + region_left + (image_check2.shape[1] / 2))
        y_center = int(loc2[0][0] + region_top + (image_check2.shape[0] / 2))
        click(x_center, y_center)  # Perform a mouse click at the center of the found image
        time.sleep(0.02)  # Add a small delay for stability
        return True
    else:
        return False

# Create the main application window
root = tk.Tk()
root.title("Screenshot Capture")

# Create a button for taking a screenshot
screenshot_button = tk.Button(root, text="Start Game", command=check_and_click)
screenshot_button.pack(pady=10)

# Run the main event loop
root.mainloop()
