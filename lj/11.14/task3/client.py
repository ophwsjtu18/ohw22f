'''
Author: linin00
Date: 2022-11-14 21:18:41
LastEditTime: 2022-11-14 21:52:46
LastEditors: linin00
Description: 
FilePath: /lj/11.14/task3/client.py

'''
import sys
sys.path.append('./utils')
from Hand import Gesture2Direction
from cv2Utils import Camera
from cv2Utils import waitKey
import cv2
from serialUtils import Serial
serial = Serial('/dev/ttys008')
from cv2Face2Dir import Direction

if __name__ == '__main__':
  camera = Camera()
  detector = Gesture2Direction()
  while True:
    img = camera.read()
    dir = detector.direction(img)
    command:str
    if dir == Direction.FORWARD :
      command = 'forward\n'
    elif dir == Direction.BACKWARD :
      command = 'backward\n'
    elif dir == Direction.LEFT :
      command = 'left\n'
    elif dir == Direction.RIGHT :
      command = 'right\n'
    else :
      command = 'standby\n'
    cv2.imshow('img', img)
    serial.write(command)
    if waitKey(1, 'q'):
      break
