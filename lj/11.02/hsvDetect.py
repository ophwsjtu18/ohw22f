'''
Author: linin00
Date: 2022-11-02 18:10:06
LastEditTime: 2022-11-02 18:26:03
LastEditors: linin00
Description: 
FilePath: /lj/11.02/hsvDetect.py

'''
import cv2
import numpy as np

img=cv2.imread("./images/red.jpg")

imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower_red=np.array([1,200,100])
upper_red=np.array([8,255,255])

redobj=cv2.inRange(imghsv,lower_red,upper_red)

conts,hrc=cv2.findContours(redobj,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(conts)

img = cv2.drawContours(img, conts, -1, (0,255,0), 3)

bigconts=[]
for cont in conts:
  area = cv2.contourArea(cont)
  if area >200:
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