'''
Author: linin00
Date: 2022-11-14 21:19:21
LastEditTime: 2022-11-14 21:19:22
LastEditors: linin00
Description: 
FilePath: /lj/utils/lightUtils.py

'''
import sys
sys.path.append('./utils')
import cv2
import numpy as np
from cv2Face2Dir import Direction

class Light :
  def __init__(self):
    self.__light      = cv2.imread('./images/light.png') # (245, 200, 3)
    self.__light_gray = cv2.imread('./images/light_gray.png')
    self.__canvas = np.zeros((245 * 3 + 4 * 30, 200 * 3 + 4 * 30, 3), np.uint8) # 图片间隙为30像素
    self.__canvas.fill(255) # 使用白色填充图片区域,默认为黑色
    self.__up     = (30, 30 + 200 + 30)
    self.__mid    = (30 + 245 + 30, 30 + 200 + 30)
    self.__down   = (30 + 245 + 30 + 245 + 30, 30 + 200 + 30)
    self.__left   = (30 + 245 + 30, 30)
    self.__right  = (30 + 245 + 30, 30 + 200 + 30 + 200 + 30)
    for idx in [self.__up, self.__down, self.__left, self.__right, self.__mid] :
      self.__canvas[idx[0]: idx[0] + 245, idx[1]: idx[1] + 200] = self.__light_gray
  def show(self) :
    cv2.imshow("light", self.__canvas)
  def direction(self, dir):
    for idx in [self.__up, self.__down, self.__left, self.__right, self.__mid] :
      self.__canvas[idx[0]: idx[0] + 245, idx[1]: idx[1] + 200] = self.__light_gray
    idx = (0, 0)
    if dir == Direction.FORWARD :
      idx = self.__up
    elif dir == Direction.BACKWARD :
      idx = self.__down
    elif dir == Direction.LEFT :
      idx = self.__left
    elif dir == Direction.RIGHT :
      idx = self.__right
    else :
      idx = self.__mid
    self.__canvas[idx[0]: idx[0] + 245, idx[1]: idx[1] + 200] = self.__light