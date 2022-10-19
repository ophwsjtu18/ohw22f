import numpy as np
import cv2
import matplotlib.pyplot as plt


img=cv2.imread('VCG211262738767.jpg')
head=img[400:550,250:400].copy()
for i in range(0,400,150):
    for j in range(0,350,150):
        img[i:150+i,j:j+150]=head

b,g,r=cv2.split(img)
img2=cv2.merge([r,g,b])


plt.figure("Image")  
plt.imshow(img2)
plt.axis('off')
plt.title('tiger')

ax=plt.gca()
for i in range(0,400,150):
    for j in range(0,350,150):
        ax.add_patch(plt.Rectangle((i,j),150,150,color="green",fill=False,linewidth=3))
plt.show()

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows

#open cv 用的是BGR接口，而matplotlib.pyplot用的RGB模式，所以一个是冷色一个是暖色
