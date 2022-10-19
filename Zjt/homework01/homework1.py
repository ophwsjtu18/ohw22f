import numpy as np
import cv2

img =cv2.imread('D:\\imageCache\\tiger.png')

length=200
line_width=2

img_head=img[150:150+length-2*line_width,200:200+length-2*line_width].copy()

xbase=0
ybase=0

for i in range(0,3):
    for j in range(0,3):
        ptlefttop=(xbase,ybase)
        ptrightbottom=(xbase+length,ybase+length)
        cv2.rectangle(img,ptlefttop,ptrightbottom,(0,255,0),line_width)
        
        xstart=xbase+line_width
        xend=xbase+length-line_width

        ystart=ybase+line_width
        yend=ybase+length-line_width

        img[xstart:xend,ystart:yend]=img_head
        
        xbase=xbase+length
        
    xbase=0
    ybase=ybase+length 

cv2.imshow('tiger',img)
cv2.waitKey(0)
cv2.destroyAllWindows()