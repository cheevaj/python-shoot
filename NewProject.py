import pyautogui
from pyautogui import *
import time
import keyboard
import win32api, win32con
import cv2
import tkinter as tk
import numpy as np

# กำหนดฟล็อกเก็บว่ารูปภาพได้รับคลิกหรือยัง
image_clicked = False
def take_screenshot():
    global image_clicked
    if not image_clicked:  # ตรวจสอบว่าฟังก์ชันถูกเรียกหรือยัง
        # จับภาพหน้าจอในพื้นที่ที่ระบุ
        screenshot_1 = pyautogui.screenshot(region=(380, 370, 300, 80))  # (ซ้าย, บน, ความกว้าง, ความสูง)
        screenshot_1.save('Colors_HEX.jpg')  # บันทึกภาพหน้าจอเป็น 'Colors_HEX.jpg'
        image_clicked = True  # อัพเดทฟล็อกเพื่อระบุว่าฟังก์ชันได้รับเรียกแล้ว
        result = search_and_click()  # เรียกใช้ฟังก์ชัน search_and_click เพื่อค้นหาภาพและคลิก
        return result
    else:
        image_clicked = False  # รีเซ็ตฟล็อกเพื่ออนุญาตให้สามารถจับภาพหน้าจอใหม่และคลิกอีกครั้ง

def click(x, y):
    # ฟังก์ชันจำลองการคลิกเมาส์ที่พิกัดที่ระบุ (x, y)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# ดึงขนาดของจอภาพ
screen_width, screen_height = size()

# การกำหนดระยะห่าง
padding = 100
# คำนวณพื้นที่ใหม่
region_left = padding
region_top = padding
region_width = screen_width - 2 * padding
region_height = screen_height - 2 * padding

def start_Game():
    result = check_point()
    # อัพเดตข้อความในป้ายตรวจสอบด้วยผลลัพธ์
    result_label.config(text=result)
def check_point():
    image_start = cv2.imread('Image/money.jpg', 0)
    result = search_and_click(image_start)
    if result == True:
        check_point_2()
    else:
        print('Not Images')
def check_point_2():
    image_start = cv2.imread('Image/money.jpg', 0)
    result = search_and_click(image_start)
    if result == True:
        check_point_2()
    else:
        start_Game()
def search_and_click(image_start):
    global image_clicked
    # โหลดภาพที่ต้องการค้นหา
    image_to_find = image_start

    # จับภาพหน้าจอในพื้นที่ที่ระบุ
    pic = screenshot(region=(region_left, region_top, region_width, region_height))

    # แปลงภาพให้เป็นขาวดำ
    gray_pic = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2GRAY)

    # ใช้เทคนิคการค้นหาภาพเทมเพลตของ OpenCV เพื่อค้นหาภาพ
    res = cv2.matchTemplate(gray_pic, image_to_find, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # หากพบภาพและยังไม่ได้คลิก
    if len(loc[0]) > 0:
        # คลิกที่ตรงกลางของกรอบที่พบครั้งแรก
        x_center = int(loc[1][0] + region_left + (image_to_find.shape[1] / 2))
        y_center = int(loc[0][0] + region_top + (image_to_find.shape[0] / 2))
        click(x_center, y_center)  # โมเดลการคลิกเมาส์ที่จุดกลางของภาพที่พบ
        time.sleep(0.05)  # เพิ่มความล่าช้าเล็กน้อยเพื่อความเสถียร
        return True
    else:
        return False

# สร้างหน้าต่างหลักของแอปพลิเคชัน
root = tk.Tk()
root.title("Menu")

# สร้างปุ่มสำหรับจับภาพหน้าจอ
screenshot_button = tk.Button(root, text="Shoot", command=take_screenshot)
screenshot_button.pack(pady=10)

# สร้างปุ่มสำหรับเริ่มเกม
go_button = tk.Button(root, text="Start Game", command=start_Game)
go_button.pack(pady=10)

# สร้างป้ายเพื่อแสดงผลลัพธ์
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# ทำให้โปรแกรมเรียกใช้งานตลอดเวลา
root.mainloop()
