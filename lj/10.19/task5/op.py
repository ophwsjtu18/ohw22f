'''
Author: linin00
Date: 2022-10-19 20:01:33
LastEditTime: 2022-10-24 14:33:03
LastEditors: linin00
Description: 
FilePath: /ohw22f/LJ/10.19/task5/op.py

'''
import numpy as np
import cv2
face_model = 'haarcascade_frontalface_default.xml'
eye_model  = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade  = cv2.CascadeClassifier(eye_model)

LEFT = 1
RIGHT = 2
FORWARD = 3
BACKWARD = 4
STANDBY = 5
NOFACE = 0

left_i = cv2.imread("left.png")
right_i = cv2.imread("right.png")
backward_i = cv2.imread("backward.png")
forward_i = cv2.imread("forward.png")
standby_i = cv2.imread("standby.png")
noface_i = cv2.imread("noface.png")

def reprint(img, dir, x, y):
  text = "error"
  tmp = noface_i
  if dir == LEFT:
    text = "left"
    tmp = left_i
  elif dir == RIGHT:
    text = "right"
    tmp = right_i
  elif dir == FORWARD:
    text = "forward"
    tmp = forward_i
  elif dir == BACKWARD:
    text = "backward"
    tmp = backward_i
  elif dir == STANDBY:
    text = "standby"
    tmp = standby_i
  elif dir == NOFACE:
    return
  cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
  w = img.shape[1]
  h = img.shape[0]
  b_x = w - 50
  e_x = w
  b_y = h - 50
  e_y = h
  img[h-50:h, w-50:w]=tmp

def face2direction(img) :
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  width = img.shape[1]
  hight = img.shape[0]
  print(gray.shape)
  if (len(faces) == 1) :
    for (x, y, w, h) in faces:
      img = cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0), 2)
      mid = x + w/2
      if mid < width/3 :
        reprint(img, LEFT, x, y)
        return img, LEFT
      elif mid > 2*width/3 :
        reprint(img, RIGHT, x, y)
        return img, RIGHT
      elif w > width/3 :
        reprint(img, FORWARD, x, y)
        return img, FORWARD
      elif w < width/5 :
        reprint(img, BACKWARD, x, y)
        return img, BACKWARD
      else :
        reprint(img, STANDBY, x, y)
        return img, STANDBY

  return img, NOFACE

def handleDir(img, dir) :
  if dir == NOFACE:
    print("no face in th screen\t👻")
  elif dir == LEFT :
    print("left\t👈")
  elif dir == RIGHT :
    print("right\t👉")
  elif dir == FORWARD :
    print("forward\t🫵")
  elif dir == STANDBY :
    print("standby\t🖐")
  elif dir ==BACKWARD :
    print("backward\t🤌")
  else :
    print("something wrong")

if __name__ == "__main__":
  cap = cv2.VideoCapture(0)
  while(True):
    ret, frame = cap.read()
    img = cv2.flip(frame, 1)
    img, dir = face2direction(img)
    handleDir(img, dir)
    cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  cap.release()
  cv2.destroyAllWindows()
