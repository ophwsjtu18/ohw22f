import numpy as np
import  cv2
img = cv2.imread('./2022-10-12-19-53-41.png')


head=img[100:200,200:300].copy()

for i in range(3):
    for j in range(3):
        img[(j)*100:(j+1)*100,(i)*100:(i+1)*100]=head
        
for i in range(3):
    for j in range(3):
        cv2.rectangle(img,(j*100,i*100),((j+1)*100,(i+1)*100),(0,255,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
