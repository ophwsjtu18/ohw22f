'''
Author: linin00
Date: 2022-11-08 21:21:20
LastEditTime: 2022-11-08 23:18:21
LastEditors: linin00
Description: 
FilePath: /lj/11.08/homework/homework.py

'''
import sys
sys.path.append("utils")
import cv2
from cv2Face2Dir import Direction
from MXMqtt import MXMqtt
from Hand import Gesture2Direction
from cv2Utils import Camera
from mcUtils import MC

class HW :
  def __init__(self):
    self.__camera = Camera()
    self.__gesture2Direction = Gesture2Direction()
    self.__mqtt = MXMqtt("mqtt.16302.com", 1883)
    self.__mc = MC()
  def solution(self):
    while(True):
      img = self.__camera.read()
      dir = self.__gesture2Direction.direction(img)
      print(dir)
      cv2.imshow('frame', img)
      self.__mc.move(dir)
      self.__mqttMsg(dir)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
  def __mqttMsg(self, dir):
    text = ""
    if dir == Direction.FORWARD:
      text = "TOP"
    elif dir == Direction.BACKWARD:
      text = "DOWN"
    elif dir == Direction.LEFT:
      text = "LEFT"
    elif dir == Direction.RIGHT:
      text = "RIGHT"
    elif dir == Direction.STANDBY:
      text = "STAND_BY"
    self.__mqtt.PUB("LJ", text)

if __name__ == '__main__':
  hw = HW()
  hw.solution()