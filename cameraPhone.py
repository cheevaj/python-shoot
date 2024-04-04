import cv2

# Replace 'IP_ADDRESS' with the IP address provided by IP Webcam app
url = 'http://10.107.56.52:8080/video'

# Open the video stream
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Failed to open the video stream")

while True:
    # Read frame from the video stream
    ret, frame = cap.read()

    if not ret:
        print("Failed to receive frame from the camera")
        break

    # Resize the frame to have a height and width of 400 pixels
    frame = cv2.resize(frame, (500, 400))

    # Display the frame
    cv2.imshow('Camera', frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
