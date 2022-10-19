'''
Author: linin00
Date: 2022-10-19 19:40:54
LastEditTime: 2022-10-19 19:47:29
LastEditors: linin00
Description: 
FilePath: /openhw/10.19/task4/file.py

'''
import numpy as np
import cv2
face_model = 'haarcascade_frontalface_default.xml'
eye_model  = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade  = cv2.CascadeClassifier(eye_model)

def demo(img) :
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
    return img

url = "tvb.flv"
cap = cv2.VideoCapture(url)
while(True):
  ret, frame = cap.read()
  img = cv2.flip(frame, 1)
  img = demo(frame)
  cv2.imshow('frame', img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()