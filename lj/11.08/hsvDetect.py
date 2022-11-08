'''
Author: linin00
Date: 2022-11-08 14:16:33
LastEditTime: 2022-11-08 16:00:11
LastEditors: linin00
Description: 
FilePath: /lj/11.08/hsvDetect.py

'''
import cv2
import numpy as np
from cv2Utils import Camera
import cv2

img=cv2.imread("./images/red.jpg")

imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# 色调 饱和度 名度
lower_red=np.array([1,200,100])
upper_red=np.array([8,255,255])

redobj=cv2.inRange(imghsv,lower_red,upper_red) # 输出二值图

conts, hrc=cv2.findContours(redobj, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # 检测二值图的轮廓
print(conts)

# img = cv2.drawContours(img, conts, -1, (0,255,0), 3) # 在原图上绘制轮廓线

bigconts=[]
for cont in conts:
  area = cv2.contourArea(cont) # 计算轮廓面积
  if area > 200:
    bigconts.append(cont)

for bigcnt in bigconts:
  M=cv2.moments(bigcnt)
  cx=int(M['m10']/M['m00'])
  cy=int(M['m01']/M['m00'])
  cv2.circle(img,(cx,cy),100,(0,0,255),5)

img = cv2.drawContours(img, bigconts, -1, (255,0,0), 10)

cv2.imshow("redobj",redobj)
cv2.imshow("myshowwindwos",img)

cv2.waitKey(0)
cv2.destroyAllWindows()