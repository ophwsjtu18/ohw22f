'''
Author: linin00
Date: 2022-10-24 14:37:56
LastEditTime: 2022-10-24 14:44:49
LastEditors: linin00
Description: 
FilePath: /ohw22f/lj/10.24/face.py

'''
import numpy as np
import cv2
face_model = 'haarcascade_frontalface_default.xml'
eye_model  = 'haarcascade_eye.xml'
image_file = 'xiuxiuman.png'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade  = cv2.CascadeClassifier(eye_model)

if __name__ == '__main__':
  img = cv2.imread(image_file)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x, y, w, h) in faces:
    img = cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
      cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
  cv2.imshow('img', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
