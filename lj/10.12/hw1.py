import numpy as np
import cv2
import copy
img = cv2.imread('tiger.jpeg',0)
print(img.shape)
head1=img[53:113, 155:215]
head=copy.copy(head1)
cv2.rectangle(head, (0, 0), (60, 60), (0, 255, 0),3)
for i in range(0, 3):
 for j in range(0, 3):
  img[60*i:60*i+60, 60*j:60*j+60]=head
cv2.imshow('image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
