import pyautogui
import time
import tkinter as tk
def take_screenshot():
    # Capture the screenshot of the first specified region
    screenshot_1 = pyautogui.screenshot(region=(865, 302, 190, 185)) # (left, top, width, height)
    # Save the first screenshot
    screenshot_1.save('Image_one.jpg')
    print("First screenshot of the story content captured and saved as 'story_screenshot.png'")

    # Capture the screenshot of the second specified region
    screenshot_2 = pyautogui.screenshot(region=(805, 402, 200, 185)) # (left, top, width, height)
    # Save the second screenshot
    screenshot_2.save('Image_two.jpg')

    print("Second screenshot of the story button captured and saved as 'story_button.jpg'")

# Create the main application window
root = tk.Tk()
root.title("Screenshot Capture")

# Create a button for taking the screenshot
screenshot_button = tk.Button(root, text="Shoot", command=take_screenshot)
screenshot_button.pack(pady=10)

# Run the main event loop
root.mainloop()
