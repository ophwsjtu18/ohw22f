'''
Author: linin00
Date: 2022-11-02 12:17:04
LastEditTime: 2022-11-02 18:06:45
LastEditors: linin00
Description: 
FilePath: /lj/11.02/hwplus/hwplus.py

'''
from mcpi.minecraft import Minecraft
import sys
sys.path.append("utils")
sys.path.append("11.01")
import Hand
import cv2
import time
from cv2Face2Dir import Direction
from hw import Cross
from MXMqtt import MXMqtt
from Hand import Hand2Direction

class HW :
  def __init__(self):
    self.__cap = cv2.VideoCapture(0)
    self.__hand2direction = Hand2Direction()
    self.__mc = Minecraft.create()
    self.__mqtt = MXMqtt("mqtt.16302.com", 1883)

  def solution(self):
    pos=self.__mc.player.getTilePos()
    print("player pos is",pos)
    cross = Cross(pos.x, pos.y, pos.z)
    while(True):
      ret, frame = self.__cap.read()
      img = cv2.flip(frame, 1)
      dir = self.__hand2direction.direction(img, 8)
      cv2.imshow('frame', img)
      cross.direction(dir)
      cross.showCross()
      self.__mqttMsg(dir)
      print(dir)
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