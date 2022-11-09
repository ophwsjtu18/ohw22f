from asyncio.windows_events import NULL
from enum import Enum
import numpy as np
import cv2
import serial
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

class Direction(Enum):
    left=1
    right=2
    forward=3
    back=4

def Img_Change(img,direction):
    if(direction==None or direction==NULL):
        return
    dirimg = cv2.imread(str(direction.name)+'.png')
    newdirimg = cv2.resize(dirimg,(50,50), interpolation=cv2.INTER_AREA)
    
    w,h,d=img.shape
    wn,hn,dn = newdirimg.shape

    tmp = newdirimg[0:hn,0:wn]
    img[w-wn:w,h-hn:h]=tmp

    return

def Face_Recognition(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)


    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return faces

def Face_Direction(shape,faces):
    if(len(faces)==0):
        return

    height,width,deepth = shape
    
    leftLimit = width/3
    rightLimit = width*2/3

    maxLimitW = width/1.5
    maxLimitH = height/1.5

    minLimitW = width/2.5
    minLimitH = height/2.5

    direction = NULL
    for (x,y,w,h) in faces:
        horLocation=x+w/2
        if(horLocation<leftLimit):
            direction = Direction.left
        elif(horLocation>rightLimit):
            direction = Direction.right
        elif(w>maxLimitW or h>maxLimitH):
            direction = Direction.forward
        elif(w<minLimitW or h<minLimitH): 
            direction = Direction.back

    return direction

ser = serial.Serial('COM2')

cap = cv2.VideoCapture(0)

i = 5
while(True):
    
    ret,frame = cap.read()
    
    #frame = cv2.flip(frame,1)
    
    imgshape=frame.shape
    
    faces=Face_Recognition(frame)
    direction = Face_Direction(imgshape,faces)
    
    if(direction):
        i = i-1
        print(direction.name)
        print(i)
        if(i == 0):
            ser.write((direction.name+'\n').encode())
            print(direction.name)
            i = 5;
    Img_Change(frame,direction)
    cv2.imshow('img',frame)
    if cv2.waitKey(50) & 0xFF == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()