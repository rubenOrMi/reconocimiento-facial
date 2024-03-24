import cv2 as cv
import numpy as np
import math

face = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)
i = 0
while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        #frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        frame2 = frame[y-10:y + h +10, x-10:x + w +10]
        #frame2 = escala(frame2,50)
        frame2 = cv.resize(frame2, (100, 100), interpolation=cv.INTER_AREA)
        #cv.imshow('frame', frame2)
        cv.imwrite("caras/ruben/ruben" + str(i) + ".png", frame2)
    cv.imshow('faces', frame)
    i = i + 1
    k = cv.waitKey(1)
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
