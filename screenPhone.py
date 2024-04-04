import cv2
import numpy as np
import pyautogui

screen_width, screen_height = pyautogui.size()
screen_bbox = (0, 0, screen_width, screen_height)
display_width = 1200
display_height = 800
try:
    while True:
        screen = pyautogui.screenshot(region=screen_bbox)
        screen_np = np.array(screen)
        screen_bgr = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
        resized_frame = cv2.resize(screen_bgr, (display_width, display_height))
        cv2.imshow('Screen Capture', resized_frame)
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    cv2.destroyAllWindows()
