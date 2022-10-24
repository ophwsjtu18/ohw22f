import numpy as np
import cv2
face_model = 'haarcascade_frontalface_default.xml'
eye_model  = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade  = cv2.CascadeClassifier(eye_model)

NOFACE = 0
LEFT = 1
RIGHT = 2
FORWARD = 3
BACKWARD = 4
STANDBY = 5


left = cv2.imread("left.png")
right = cv2.imread("right.png")
backward = cv2.imread("backward.png")
forward = cv2.imread("forward.png")
standby = cv2.imread("standby.png")
noface = cv2.imread("noface.png")

def display(img, dir):
  tmp = noface
  w = img.shape[1]
  h = img.shape[0]
  if dir == LEFT:
    tmp = left
  elif dir == RIGHT:
    tmp = right
  elif dir == FORWARD:
    tmp = forward
  elif dir == BACKWARD:
    tmp = backward
  elif dir == STANDBY:
    tmp = standby
  elif dir == NOFACE:
    tmp = noface

  img[h-100:h,w-100:w]=tmp

def face2direction(img) :
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 3)
  width = img.shape[1]
  if(len(faces) != 0):
    for (x, y, w, h) in faces:
      img = cv2.rectangle(img,(x, y), (x+w, y+h), (255, 0, 0), 2)
      mid = x + w/2
      if mid < width/3 :
        return img, LEFT
      elif mid > 2*width/3 :
        return img, RIGHT
      elif w > width/5 :
        return img, FORWARD
      elif w < width/6 :
        return img, BACKWARD
      else :
        return img, STANDBY

  return img, NOFACE

cap = cv2.VideoCapture(1)
while(True):
  ret, frame = cap.read()
  img = cv2.flip(frame, 1)
  img, dir = face2direction(img)
  display(img,dir)
  cv2.imshow('frame', img)
  if cv2.waitKey(10) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()