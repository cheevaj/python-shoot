import pyautogui
from pyautogui import *
import time
import keyboard
import win32api, win32con
import cv2
import tkinter as tk
import numpy as np

# Initialize flag to keep track of whether the image has been clicked
image_clicked = False

def take_screenshot():
    global image_clicked
    if not image_clicked:  # Check if the function has already been called
        # Capture a screenshot of the specified region
        screenshot_1 = pyautogui.screenshot(region=(380, 370, 300, 80))  # (left, top, width, height)
        screenshot_1.save('Colors_HEX.jpg')  # Save the screenshot as 'Colors_HEX.jpg'
        image_clicked = True  # Update the flag to indicate that the function has been called
        search_and_click()  # Call the search_and_click function to perform image search and click
    else:
        image_clicked = False  # Reset the flag to allow taking a new screenshot and clicking again

def click(x, y):
    # Function to simulate a mouse click at specified coordinates (x, y)
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
region_width = screen_width - 2 * padding
region_height = screen_height - 2 * padding

# Load the image to be searched
image_to_find = cv2.imread('Colors_HEX.jpg', 0)

def search_and_click():
    global image_clicked
    # Load the image to be searched (reload it each time to use the latest screenshot)
    image_to_find = cv2.imread('Colors_HEX.jpg', 0)

    # Capture the screenshot of the specified region
    pic = screenshot(region=(region_left, region_top, region_width, region_height))

    # Convert the screenshot to grayscale
    gray_pic = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2GRAY)

    # Use OpenCV template matching to find the image
    res = cv2.matchTemplate(gray_pic, image_to_find, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # If image found and not clicked yet, click on it
    if len(loc[0]) > 0:
        # Click on the middle of the first found bounding box
        x_center = int(loc[1][0] + region_left + (image_to_find.shape[1] / 2))
        y_center = int(loc[0][0] + region_top + (image_to_find.shape[0] / 2))
        click(x_center, y_center)  # Perform a mouse click at the center of the found image
        time.sleep(0.02)  # Add a small delay for stability

# Create the main application window
root = tk.Tk()
root.title("Screenshot Capture")

# Create a button for taking a screenshot
screenshot_button = tk.Button(root, text="Ok", command=take_screenshot)
screenshot_button.pack(pady=10)

# Create a button for searching and clicking the image
go_button = tk.Button(root, text="Go", command=search_and_click)
go_button.pack(pady=10)

# Run the main event loop
root.mainloop()
