import numpy as num
import cv2

img = cv2.imread('Tiger.jpg')

head = img[220:570,40:360].copy()
cv2.rectangle(head,(0,0),(318,347),(0,255,0),3)

for i in range(0,3):
    for j in range(0,3):
        img[i*350:(i+1)*350,j*320:(j+1)*320] = head

cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.imwrite('Result.png',img)
cv2.destroyAllWindows()