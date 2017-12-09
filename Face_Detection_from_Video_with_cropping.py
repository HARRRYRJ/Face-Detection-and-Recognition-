import numpy as np
import cv2
import sys
#put your opencv path
face_cascade = cv2.CascadeClassifier('/home/vishal/opencv/data/haarcascades/haarcascade_frontalface.xml')
eye_cascade = cv2.CascadeClassifier('/home/vishal/opencv/data/haarcascades/haarcascade_eye.xml')

#img = cv2.imread('sachin.jpg') #if you want to crop an image then use this line otherwise ignore this line.
#capturing video from your webcam
video_capture = cv2.VideoCapture(0)
count = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)

    )

    # Draw a rectangle around the faces and crop and save
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)
        crop_img = frame[y : y+h, x : x+w]
        cv2.imwrite("Vishal.%d.jpg" % count, crop_img)     # save frame as JPEG file
        count += 1


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video_capture.release()
cv2.destroyAllWindows()


