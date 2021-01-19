# Face Detector

In this repository you will see how to easy code a face detector app by using OpenCV (available here: https://github.com/opencv/opencv).
It mainly works with the haar cascade algorithm.

The repository consists in a beginner program that trains an artificial intelligence to detect faces, both in a video or in a photo.

**facedetection.py**
The code is done with the image given in the repository. If the user want to find faces in other images, he/she just has to change the path in line 8.

**video_facedetection.py**
In my case, the video was the default webcam recording, so that's why the parameter in VideoCapture(0).

In this case, we loop for every frame while the video is on. As soon as we press Q, the program stops.

If you want to visualize how the OpenCV works, you can check this video: https://www.youtube.com/watch?v=hPCTwxF0qf4&t=119s&ab_channel=AnkurDivekar
