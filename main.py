import pyautogui
import time
import keyboard
import win32api, win32con
import cv2
import tkinter as tk
import numpy as np

# Initialize flag to keep track of whether the image has been clicked
image_clicked = False

def take_screenshot(name, screenshot_size, image_point1):
    global image_clicked
    if not image_clicked:  # Check if the function has already been called
        # Capture a screenshot of the specified region
        screenshot_1 = pyautogui.screenshot(region=screenshot_size)  # (left, top, width, height)
        screenshot_1.save(name)  # Save the screenshot as 'Colors_HEX.jpg'
        image_clicked = True  # Update the flag to indicate that the function has been called
        return True
    else:
        image_clicked = False  # Reset the flag to allow taking a new screenshot and clicking again
        return False

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

def start_Game():
    result = check_point()  # Pass name and screenshot_size as arguments
    # Update the label text with the result
    result_label.config(text=result)

def check_point():
    # Load the images
    image_start1 = cv2.imread('Image/money.jpg', 0)
    image_start2 = cv2.imread('Image/time.jpg', 0)
    # Check if the images are found and clicked
    result = search_and_click(image_start1, image_start2)
    if result:
        root.after(500, check_point_2)  # Delay execution of check_point_2 by 1 minute (60 seconds)
    else:
        print('No Images Found')

def check_point_2():
    # Load the image
    image_point1 = cv2.imread('Image/remenber_image.jpg', 0)
    name = 'Image_P1.jpg'
    screenshot_size = (865, 302, 190, 185)
    shoot = take_screenshot(name, screenshot_size, image_point1)
    if shoot:
        image_start1 = cv2.imread('Image/Next_game1.jpg', 0)
        image_start2 = cv2.imread('Image/Next_game1.jpg', 0)
        # Delay the execution of search_and_click by 700 milliseconds
        root.after(500, lambda: search_and_click_delayed(image_start1, image_start2))
    else:
        start_Game()

def search_and_click_delayed(image1, image2):
    result = search_and_click(image1, image2)
    if result:
        check_and_click()
    else:
        print("Next_game1 not found.")

def check_and_click():
    image_check1 = cv2.imread('Image_P1.jpg', 0)
    image_check2 = cv2.imread('Image/test2.jpg', 0)
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

def search_and_click(image1, image2):
    global image_clicked
    # Capture the screenshot of the specified region
    pic = pyautogui.screenshot(region=(region_left, region_top, region_width, region_height))

    # Convert the screenshot to grayscale
    gray_pic = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2GRAY)

    # Use OpenCV template matching to find the first image
    res1 = cv2.matchTemplate(gray_pic, image1, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc1 = np.where(res1 >= threshold)

    # Use OpenCV template matching to find the second image
    res2 = cv2.matchTemplate(gray_pic, image2, cv2.TM_CCOEFF_NORMED)
    loc2 = np.where(res2 >= threshold)

    # If both images are found, click on the first image
    if len(loc1[0]) > 0 and len(loc2[0]) > 0:
        # Click on the middle of the first found bounding box of the first image
        x_center = int(loc1[1][0] + region_left + (image1.shape[1] / 2))
        y_center = int(loc1[0][0] + region_top + (image1.shape[0] / 2))
        click(x_center, y_center)  # Perform a mouse click at the center of the found image
        time.sleep(0.02)  # Add a small delay for stability
        return True
    else:
        return False

# Create the main application window
root = tk.Tk()
root.title("Screenshot Capture")

# Create a button for taking a screenshot
screenshot_button = tk.Button(root, text="start Game", command=start_Game)
screenshot_button.pack(pady=10)

screenshot_button = tk.Button(root, text="click image", command=check_and_click)
screenshot_button.pack(pady=10)
# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
