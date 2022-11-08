'''
Author: linin00
Date: 2022-11-08 16:07:29
LastEditTime: 2022-11-08 16:14:38
LastEditors: linin00
Description: 
FilePath: /lj/utils/fpsUtils.py

'''
import cv2
import time
class FPS:
  def __init__(self):
    super()
    self.__ctime = 0
    self.__ptime = 0
    self.__fps = 0
  def __titok(self):
    self.__ctime = time.time()
    self.__fps = 1 / (self.__ctime - self.__ptime)
    self.__ptime = self.__ctime
  def printFps(self, img):
    self.__titok()
    cv2.putText(img, str(int(self.__fps)), (10, 70), 
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)