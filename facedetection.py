import cv2
from random import randrange

# Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Choose an image to detect the face in it
img = cv2.imread('C:/Users/Usuario/Documents/courses/MachineLearning/facedetection/multiple_faces.jpg')

# To better the detection, we convert the image to grayscale
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

# print(face_coordinates)

# Draw rectangles around the faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the image with faces detected
cv2.imshow('Clever Programmer Face Detector', img)

cv2.waitKey()
print("Code Completed")