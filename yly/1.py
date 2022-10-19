import numpy as np
import cv2

img=cv2.imread('1.jpg')
head=img[70:120,100:150].copy()
for i in range(1,4):
    for j in range(1,4):
        img[50*(i-1):50*i,50*(j-1):50*(j)]=head
for i in range(1,4):
    for j in range(1,4):
        cv2.rectangle(img,(50*(i-1),50*(j-1)),(50*i,50*(j)),(255,255,200),1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
