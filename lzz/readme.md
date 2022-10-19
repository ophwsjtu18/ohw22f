# 李治璋 519021910171
## 第一次作业
原图
<img src="./cats.jpeg" width="1000px">

效果图
<img src="./tiger1.jpeg" width="1000px">

源代码如下，详见[test1.ipynb](./test1.ipynb)
```
import cv2
img=cv2.imread("cats.jpeg")

t=img[100:600,400:800].copy()
print(t.shape)
q=cv2.resize(t,(120,150))
print(q.shape)

for i in range(0,3):
    for j in range(0,3):
        img[0+150*i:150+150*i,0+120*j:120+120*j]=q
        cv2.rectangle(img,(0+120*j,0+150*i),(120+120*j,150+150*i),(0,255,0),3)

img=cv2.resize(img,(168*5,105*5))
cv2.imshow("Cats",img)
cv2.imwrite('tiger1.jpeg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
