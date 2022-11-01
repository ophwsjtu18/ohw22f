'''
Author: linin00
Date: 2022-11-01 21:37:04
LastEditTime: 2022-11-01 22:21:19
LastEditors: linin00
Description: 
FilePath: /lj/utils/cv2Face2Dir.py

'''
import numpy as np
import cv2
from enum import Enum

class Direction(Enum):
  NOFACE = 0
  LEFT = 1
  RIGHT = 2
  FORWARD = 3
  BACKWARD = 4
  STANDBY = 5

class cv2Face2Dir():
  def __init__(self):
    face_model = 'utils/model/haarcascade_frontalface_default.xml'
    eye_model  = 'utils/model/haarcascade_eye.xml'
    self.__face_cascade = cv2.CascadeClassifier(face_model)
    self.__eye_cascade  = cv2.CascadeClassifier(eye_model)
  def __drawDirection(self, img, direction, x, y):
    left_i = cv2.imread("utils/img/left.png")
    right_i = cv2.imread("utils/img/right.png")
    backward_i = cv2.imread("utils/img/backward.png")
    forward_i = cv2.imread("utils/img/forward.png")
    standby_i = cv2.imread("utils/img/standby.png")
    noface_i = cv2.imread("utils/img/noface.png")
    text = ""
    tmp = noface_i
    if direction == Direction.LEFT:
      text = "left"
      tmp = left_i
    elif direction == Direction.RIGHT:
      text = "right"
      tmp = right_i
    elif direction == Direction.FORWARD:
      text = "forward"
      tmp = forward_i
    elif direction == Direction.BACKWARD:
      text = "backward"
      tmp = backward_i
    elif direction == Direction.STANDBY:
      text = "standby"
      tmp = standby_i
    elif direction == Direction.NOFACE:
      return
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
    w = img.shape[1]
    h = img.shape[0]
    b_x = w - 50
    e_x = w
    b_y = h - 50
    e_y = h
    img[h-50:h, w-50:w]=tmp

  def track(self, img, show = True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = self.__face_cascade.detectMultiScale(gray, 1.3, 5)
    width = img.shape[1]
    hight = img.shape[0]
    direction = Direction.NOFACE
    if (len(faces) == 1) :
      (x, y, w, h) = faces[0]
      if show :
        img = cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0), 2)
      mid = x + w/2
      if mid < width/3 :
        direction = Direction.LEFT
      elif mid > 2*width/3 :
        direction = Direction.RIGHT
      elif w > width/3 :
        direction = Direction.FORWARD
      elif w < width/5 :
        direction = Direction.BACKWARD
      else :
        direction = Direction.STANDBY
      if show :
        self.__drawDirection(img, direction, x, y)
    return img, direction
if __name__ == "__main__":
  cap = cv2.VideoCapture(0)
  face2direction = cv2Face2Dir()
  while(True):
    ret, frame = cap.read()
    img = cv2.flip(frame, 1)
    img, dir =face2direction.track(img)
    cv2.imshow('frame', img)
    print(dir)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  cap.release()
  cv2.destroyAllWindows()
