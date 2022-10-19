import numpy as py
import cv2

img = cv2.imread("D:\Coding_Files\PycharmProjects\pythonProject\Bengal-Tiger.webp")
head = img[160:420, 40:300].copy()  # copy pic by pixels, 1st: vertical ,2nd: horizontal;0,0 means top left corner
for i in range(1, 4):  # cautious about the tab, 1,4 means 1<=i<4
    for j in range(1, 4):
        img[260 * (i - 1):260 * i, 260 * (j - 1):260 * j] = head    # copy back to the pic
for i in range(1, 4):  # cautious about the tab, 1,4 means 1<=i<4
    for j in range(1, 4):
        cv2.rectangle(img,(260 * (i - 1),260 * (j - 1)),(260 * i,260 * j),(0,255,0),3)
        # draw green rectangle, addr, top left, bottom right, color, thickness


print(img.shape)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
