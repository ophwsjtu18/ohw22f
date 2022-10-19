'''
Author: linin00
Date: 2022-10-19 19:19:03
LastEditTime: 2022-10-19 19:35:27
LastEditors: linin00
Description: 
FilePath: /openhw/10.19/task3/realtime.py

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

url = "http://admin:admin@192.168.2.107:8081"
cap = cv2.VideoCapture(url)
# cap = cv2.VideoCapture(0)
while(True):
  ret, frame = cap.read()
  img = cv2.flip(frame, 1)
  img = demo(frame)
  cv2.imshow('frame', img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()