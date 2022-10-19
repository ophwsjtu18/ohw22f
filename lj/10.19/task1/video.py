'''
Author: linin00
Date: 2022-10-19 18:41:25
LastEditTime: 2022-10-19 18:58:52
LastEditors: linin00
Description: 读取摄像头、转化为灰度图、镜像
FilePath: /openhw/10.19/video.py

'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  frame_x = cv2.flip(frame, 0)
  frame_y = cv2.flip(frame, 1)
  cv2.imshow('frame', frame_y)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()