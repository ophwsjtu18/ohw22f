import numpy as np
import cv2

img1 = cv2.imread('tiger.jpg')
img2 = cv2.imread('tiger.jpg')
for i in [0,100,200]:
    for j in [0,100,200]:
        img2[i:i+100,j:j+100]=img1[80:180,185:285]
        cv2.rectangle(img2, (j, i), (j+100, i+100), (0, 255, 0), 2)

cv2.imshow('image', img2)
cv2.waitKey(0)

