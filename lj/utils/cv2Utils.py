'''
Author: linin00
Date: 2022-11-08 15:10:34
LastEditTime: 2022-11-08 15:17:36
LastEditors: linin00
Description: 
FilePath: /lj/utils/cv2Utils.py

'''
import cv2

class Camera:
  def __init__(self, idx = 0):
    super()
    self.__cap = cv2.VideoCapture(idx)
  def read(self, flip = True):
    success, img = self.__cap.read()
    if flip :
      img = cv2.flip(img, 1)
    return img

def waitKey(time, key):
  return cv2.waitKey(1) & 0xff == ord(key)