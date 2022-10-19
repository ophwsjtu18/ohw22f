import numpy as np
import cv2 as cv
img = cv.imread('myopencv\photo_sourse\Tiger.jpg')
head = img[120:270,550:730].copy()
for i in range(0,3):
    for j in range(0,3):
            img[150*i+3*(i+1):153*(i+1),180*j+3*(j+1):183*(j+1)]=head
            cv.rectangle(img,[183*i,153*j],[183*(i+1),153*(j+1)],(0,255,0),2)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
