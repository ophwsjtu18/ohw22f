import numpy as np
import  cv2

img = cv2.imread('./2022-10-12-19-53-41.png')

head=img[100:200,200:300].copy()
cv2.rectangle(head,(0,0),(100,100),(0,255,0),3)

for i in range(3):
    for j in range(3):
        img[(j)*100:(j+1)*100,(i)*100:(i+1)*100]=head
       
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
