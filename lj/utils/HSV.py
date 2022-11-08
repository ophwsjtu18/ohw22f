'''
Author: linin00
Date: 2022-11-08 14:54:06
LastEditTime: 2022-11-08 15:32:27
LastEditors: linin00
Description: 
FilePath: /lj/utils/HSV.py

'''
import cv2
import numpy as np
class HSVDetector :
  def __init__(self):
    super()
  def detect(self, img,
      lower = np.array([1,200,100]),
      upper = np.array([8,255,255]),
      draw = True,
      minArea = 200):
    imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    redobj=cv2.inRange(imghsv,lower,upper) # 输出二值图

    conts, hrc=cv2.findContours(redobj, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 检测二值图的轮廓
    self.__bigconts=[]
    for cont in conts:
      area = cv2.contourArea(cont) # 计算轮廓面积
      if area > minArea:
        self.__bigconts.append(cont)
    if draw :
      for bigcnt in self.__bigconts:
        M=cv2.moments(bigcnt)
        cx=int(M['m10']/M['m00'])
        cy=int(M['m01']/M['m00'])
        cv2.circle(img,(cx,cy),200,(0,0,255),5)
      img = cv2.drawContours(img, self.__bigconts, -1, (255,0,0), 10)
    return img, self.__bigconts

if __name__ == '__main__':
  detector = HSVDetector()
  img = cv2.imread('./images/red.jpg')
  img, _ = detector.detect(img)
  cv2.imshow("myshowwindwos",img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()