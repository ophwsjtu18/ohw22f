'''
Author: linin00
Date: 2022-11-08 22:37:25
LastEditTime: 2022-11-08 23:15:54
LastEditors: linin00
Description: 
FilePath: /lj/utils/mcUtils.py

'''
from mcpi.minecraft import Minecraft
import sys
sys.path.append("utils")
from cv2Face2Dir import Direction
import pyautogui
import pygetwindow

class MC :
  def __init__(self) :
    self.__mc = Minecraft.create()
    self.__dir = Direction.STANDBY
  def move(self, dir = Direction.FORWARD):
    if not self.isInMC() :
      return
    print(dir)
    if dir != self.__dir:
      pyautogui.keyUp('w')
      pyautogui.keyUp('s')
      pyautogui.keyUp('a')
      pyautogui.keyUp('d')
      if dir == Direction.FORWARD :
        pyautogui.keyDown('w')
      elif dir == Direction.BACKWARD :
        pyautogui.keyDown('s')
      elif dir == Direction.LEFT :
        pyautogui.keyDown('a')
      elif dir == Direction.RIGHT :
        pyautogui.keyDown('d')
    self.__dir = dir
  def isInMC(self):
    window = pygetwindow.getActiveWindow()
    # print(window)
    if window == 'java Minecraft 1.17.1 - 多人游戏（第三方服务器）':
        return True
    return False

if __name__ == "__main__":
  mc = MC()
  while(True) :
    mc.move()
  print("hello world!")