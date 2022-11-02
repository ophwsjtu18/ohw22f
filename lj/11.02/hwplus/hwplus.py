'''
Author: linin00
Date: 2022-11-02 12:17:04
LastEditTime: 2022-11-02 13:06:53
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

class Hand2Direction():
  def __init__(self):
    self.__hand = Hand.HandDetector()
  def __help(self, shape, pos):
    w, h = shape
    x, y = pos
    p1 = (w/3, h/3)
    p2 = (2 * w/3, h/3)
    p3 = (w/3, 2 * h/3)
    p4 = (2 * w/3, 2 * h/3)
    if x > p1[0] and x < p2[0] and y < p3[1] and y > p1[1]:
      return Direction.STANDBY
    if x < p1[0] :
      if y > p3[1] and y < p1[1]:
        return Direction.LEFT
      if y > p1[1] and x/y < w/h :
          return Direction.LEFT
      if y < p3[1] and x/(h - y) < w/h :
          return Direction.LEFT
    if x > p2[0]:
      if y > p3[1] and y < p1[1]:
        return DIRECTION.RIGHT
      if y > p1[1] and (w - x)/h < w/h :
          return Direction.RIGHT
      if y < p3[1] and (w - x)/(h - y) < w/h :
          return Direction.RIGHT
    if y > p3[1] :
      return Direction.BACKWARD
    if y < p1[1] :
      return Direction.FORWARD

  def direction(self, img, index, draw = True):
    h, w = img.shape[0], img.shape[1]
    self.__hand.findHands(img, draw)
    pos = self.__hand.trackLandmark(img, index, draw)
    print(h, w)
    print(pos)
    if len(pos) != 1 :
      return Direction.NOFACE
    rx, ry = pos[0][1], pos[0][2]
    return self.__help((w, h), (rx, ry))

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