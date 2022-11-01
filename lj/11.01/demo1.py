'''
Author: linin00
Date: 2022-11-01 08:44:42
LastEditTime: 2022-11-01 22:40:09
LastEditors: linin00
Description: 
FilePath: /lj/11.01/demo1.py

'''
from mcpi.minecraft import Minecraft
import sys
sys.path.append("utils")
import cv2Face2Dir
from MXMqtt import MXMqtt
import cv2

Direction = cv2Face2Dir.Direction

class Cross :
  def __init__(self, x = 0, y =  0, z = 0) :
    self.down = [(x, y, z), 1]
    self.mid  = [(x, y + 1, z), 1]
    self.right   = [(x, y + 1, z + 1), 1]
    self.left = [(x, y + 1, z - 1), 1]
    self.up = [(x, y + 2, z), 1]
    self.__mc = Minecraft.create()
  def showCross(self) :
    for block in (self.down, self.mid, self.up, self.left, self.right) :
      self.__mc.setBlock(block[0][0], block[0][1], block[0][2], block[1])
  def direction(self, dir) :
    for block in (self.down, self.mid, self.up, self.left, self.right) :
      block[1] = 1
    if dir == Direction.FORWARD :
      self.up[1] = 2
    elif dir == Direction.BACKWARD :
      self.down[1] = 2
    elif dir == Direction.LEFT :
      self.left[1] = 2
    elif dir == Direction.RIGHT :
      self.right[1] = 2
    elif dir == Direction.STANDBY :
      self.mid[1] = 2

class HW :
  def __init__(self):
    self.__cap = cv2.VideoCapture(0)
    self.__face2direction = cv2Face2Dir.cv2Face2Dir()
    self.__mc = Minecraft.create()
    self.__mqtt = MXMqtt("mqtt.16302.com", 1883)

  def solution(self):
    pos=self.__mc.player.getTilePos()
    print("player pos is",pos)
    cross = Cross(pos.x, pos.y, pos.z)
    while(True):
      ret, frame = self.__cap.read()
      img = cv2.flip(frame, 1)
      img, dir = self.__face2direction.track(img)
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