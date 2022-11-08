'''
Author: linin00
Date: 2022-11-08 15:59:48
LastEditTime: 2022-11-08 16:13:16
LastEditors: linin00
Description: 
FilePath: /lj/11.08/task4.py

'''
import sys
sys.path.append('./utils')
from cv2Utils import Camera
from cv2Utils import waitKey
from yolov3Utils import YoloNet
from fpsUtils import FPS
import cv2

if __name__ == '__main__':
  camera = Camera()
  yoloNet = YoloNet()
  fps = FPS()
  while True:
    img = camera.read()
    yoloNet.process(img)
    fps.printFps(img)
    cv2.imshow("img", img)
    if waitKey(1, 'q'):
      break