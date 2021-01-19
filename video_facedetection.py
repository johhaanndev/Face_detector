import cv2
from random import randrange

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capture the video from webcam
webcam = cv2.VideoCapture(0) # 0 goes to the default cam

# Iterate forever over the frames
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Convert the frame to grayscale
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

    # Draw rectangles around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

# release the webcam
webcam.release()
print("Code Completed")