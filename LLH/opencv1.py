import numpy as np
import cv2

img = cv2.imread('tiger.jpeg')
head = img[100:250,320:470].copy() #复制纯净的图像，不会因为多次提取而重叠
x_offset = 3
y_offset = 3
for i in [0,1,2]:
    for j in [0,1,2]:
        img[150*i+x_offset:150*(i+1)+x_offset,150*j+y_offset:150*(j+1)+y_offset] = head
for i in [0,1,2]:
    for j in [0,1,2]:        
        cv2.rectangle(img,(150*i+x_offset,150*j+y_offset),(150*(i+1)+x_offset,150*(j+1)+y_offset),(0,255,0),2)
cv2.imshow('tiger1',img)
cv2.waitKey(0)
cv2.imwrite("tiger1",img)
cv2.destroyAllWindows()