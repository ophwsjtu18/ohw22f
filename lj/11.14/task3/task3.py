'''
Author: linin00
Date: 2022-11-14 20:18:14
LastEditTime: 2022-11-14 21:20:18
LastEditors: linin00
Description: 
FilePath: /lj/11.14/task3/task3.py

'''
import sys
sys.path.append('./utils')
from Hand import Gesture2Direction
from cv2Utils import Camera
from cv2Utils import waitKey
import cv2
from lightUtils import Light

if __name__ == '__main__':
  camera = Camera()
  detector = Gesture2Direction()
  light = Light()
  while True:
    img = camera.read()
    dir = detector.direction(img)
    print(dir)
    cv2.imshow('img', img)
    light.direction(dir)
    light.show()
    if waitKey(1, 'q'):
      break
