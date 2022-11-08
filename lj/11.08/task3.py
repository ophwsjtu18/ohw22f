'''
Author: linin00
Date: 2022-11-08 15:15:10
LastEditTime: 2022-11-08 16:00:21
LastEditors: linin00
Description: 
FilePath: /lj/11.08/task3.py

'''
import sys
sys.path.append('./utils')
from cv2Utils import Camera
import cv2
from HSV import HSVDetector
from cv2Utils import waitKey
import numpy as np

if __name__ == '__main__':
  camera = Camera()
  hsvDetector = HSVDetector()
  lower = np.array([1,200,100])
  upper = np.array([8,255,255])
  minArea = 200
  while True:
    img = camera.read()
    img, _ = hsvDetector.detect(img, lower, upper, minArea)
    cv2.imshow('img', img)
    if waitKey(1, 'q'):
      break