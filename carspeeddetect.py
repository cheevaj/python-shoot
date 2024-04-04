import cv2
import time
from pytube import YouTube

# Download the YouTube video
yt = YouTube('https://www.youtube.com/watch?v=ty8yUVpbSm8')
yt.streams.filter(file_extension='mp4').first().download(filename='video.mp4')

# Load the video
cap = cv2.VideoCapture('video.mp4')
# Load the car cascade classifier
car_cascade = cv2.CascadeClassifier('cars.xml')

# Coordinates of polygon in frame: [[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
coord = [[637, 352], [904, 352], [631, 512], [952, 512]]

# Distance between two horizontal lines in meters
dist = 3

while True:
    ret, img = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.8, 2)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

    # Draw lines on the frame
    cv2.line(img, (coord[0][0], coord[0][1]), (coord[1][0], coord[1][1]), (0, 0, 255), 2)  # First horizontal line
    cv2.line(img, (coord[0][0], coord[0][1]), (coord[2][0], coord[2][1]), (0, 0, 255), 2)  # Vertical left line
    cv2.line(img, (coord[2][0], coord[2][1]), (coord[3][0], coord[3][1]), (0, 0, 255), 2)  # Second horizontal line
    cv2.line(img, (coord[1][0], coord[1][1]), (coord[3][0], coord[3][1]), (0, 0, 255), 2)  # Vertical right line

    for (x, y, w, h) in cars:
        if x >= coord[0][0] and y == coord[0][1]:
            print("Car Entered.")
            tim1 = time.time()  # Initial time

        if x >= coord[2][0] and y == coord[2][1]:
            print("Car Left.")
            tim2 = time.time()  # Final time
            # Calculate speed in m/s
            print("Speed in (m/s) is:", dist / (tim2 - tim1))

    cv2.imshow('img', img)  # Display the frame

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
