from MXMqtt import MXMqtt #导入库文件
import time
import numpy as np
import cv2
import mcpi.minecraft as minecraft
import mcpi.block as block
mqtt= MXMqtt("mqtt.16302.com",1883)
mqtt.SUB("DJL")
time.sleep(1)
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
cap = cv2.VideoCapture(0)
# Capture frame-by-frame
 # Our operations on the frame come here

 # Display the resulting frame
face_cascade = cv2.CascadeClassifier("myopencv\OPENCV_LEARN\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("myopencv\OPENCV_LEARN\haarcascade_eye.xml")

while(1):
    ret, frame = cap.read()
    img = cv2.cvtColor(frame,cv2.COLOR_RGB2RGBA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.flip(img,1,img)
    if ret==True:
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mysize = gray.shape 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            dx = x-mysize[0]/2
            if((dx>=100)):
                mqtt.PUB("DJL","LEFT")
                mc.setBlock(-16, 4, -56, 0)#左
                mc.setBlock(-15, 4, -56, 0)#中
                mc.setBlock(-14, 4, -56, 57)#右
                mc.setBlock(-15, 4, -57, 0)#上
                mc.setBlock(-15, 4, -55, 0)#下
            elif(dx<=-100) :
                mqtt.PUB("DJL","RIGHT")
                mc.setBlock(-16, 4, -56, 57)#左
                mc.setBlock(-15, 4, -56, 0)#中
                mc.setBlock(-14, 4, -56, 0)#右
                mc.setBlock(-15, 4, -57, 0)#上
                mc.setBlock(-15, 4, -55, 0)#下
            elif(w>250):
                mqtt.PUB("DJL","TOP")
                mc.setBlock(-16, 4, -56, 0)#左
                mc.setBlock(-15, 4, -56, 0)#中
                mc.setBlock(-14, 4, -56, 0)#右
                mc.setBlock(-15, 4, -57, 57)#上
                mc.setBlock(-15, 4, -55, 0)#下
            elif(w<150):
                mqtt.PUB("DJL","DOWN")
                mc.setBlock(-16, 4, -56, 0)#左
                mc.setBlock(-15, 4, -56, 0)#中
                mc.setBlock(-14, 4, -56, 0)#右
                mc.setBlock(-15, 4, -57, 0)#上
                mc.setBlock(-15, 4, -55, 57)#下
            else:
                mqtt.PUB("DJL","STAND_BY")
                mc.setBlock(-16, 4, -56, 0)#左
                mc.setBlock(-15, 4, -56, 57)#中
                mc.setBlock(-14, 4, -56, 0)#右
                mc.setBlock(-15, 4, -57, 0)#上
                mc.setBlock(-15, 4, -55, 0)#下
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
da=mqtt.returnMsg()
print(da)
