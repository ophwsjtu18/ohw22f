import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
left = cv2.imread("./left.png")
right = cv2.imread("./right.png")
# cap=cv2.VideoCapture("./Desktop 2022.10.19 - 19.52.26.01.mp4")

# url = "rtsp://admin:admin@192.168.1.101:8554/live"
# print('start')
# cap = cv2.VideoCapture(url)#读取视频流

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # 逐帧捕获
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 我们在框架上的操作到这里
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 显示结果帧eq
    img = frame
    cv2.flip(img,1,img)
  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    height = img.shape[0]
    width = img.shape[1]

    for (x,y,w,h) in faces:
        mid=[x+w/2,y+h/2]
        if mid[0]<width*5/12:
            msg = "left"
            cv2.putText(img,"left",(x,y),font,0.5,(0,255,0),1)
            img[0:90,0:150] = left
            # print(msg)
        if mid[0]>width*7/12:
            msg = "right"
            cv2.putText(img,"right",(x,y),font,0.5,(0,255,0),1)
            img[0:90,0:150] = right
            # print(msg)
        
        # if mid[1]<height/3:
        #     msg = "down"
        #     print(msg)
            
        # if mid[1]>height*3/2:
        #     msg = "up"
        #     print(msg)
            
        elif w<width/6:
            msg = "backward"
            cv2.putText(img,"backword",(x,y+13),font,0.5,(0,255,0),1)

        elif w>width/3:
            msg = "forward" 
            cv2.putText(img,"forword",(x,y+13),font,0.5,(0,255,0),1)
            # print(msg) 
        else:
            msg="stand by"
            cv2.putText(img,"stand by",(x,y),font,0.5,(0,255,0),1)
        # print(msg)    
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
     
    cv2.imshow('img',img)
    # cv2.waitKey(1) 
    # cv2.destroyAllWindows()
    if cv2.waitKey(1) == ord('q'):
        break
# 完成所有操作后，释放捕获器
cap.release()
cv2.destroyAllWindows()
