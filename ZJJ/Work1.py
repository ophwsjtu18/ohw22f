import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Picture1.jpg')
head = img[10:150,150:290].copy()
for i in range(0,3):
    for j in range(0,3):
            img[143*i+3:143*(i+1),143*j+3:143*(j+1)] = head
            cv2.rectangle(img,[143*i,143*j],[143*(i+1),143*(j+1)],(0,255,0),2)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
