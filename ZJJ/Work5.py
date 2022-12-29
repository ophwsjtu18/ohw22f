from asyncio.windows_events import NULL
from enum import Enum
import numpy as np
import cv2
import serial
import time

i=5

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def change(img,direction):
    if(direction==None or direction==NULL):
        return
    d0 = cv2.imread(str(direction.name)+'.png')
    newd0 = cv2.resize(d0,(50,50), interpolation=cv2.INTER_AREA)
    
    w,h,d=img.shape
    wn,hn,dn = newd0.shape

    tmp = newd0[0:hn,0:wn]
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

class Direction(Enum):
    L=1
    R=2
    F=3
    B=4

def Face_Direction(shape,faces):
    if(len(faces)==0):
        return

    height,width,deepth = shape

    direction = NULL
    for (x,y,w,h) in faces:
        horLocation=x+w/2
        if(horLocation<width/3):
            direction = Direction.L
        elif(horLocation>width*2/3):
            direction = Direction.R
        elif(w>width*2/3 or h>height*2/3):
            direction = Direction.F
        elif(w<width*2/5 or h<height*2/5): 
            direction = Direction.B

    return direction

ser = serial.Serial('COM2')

cap = cv2.VideoCapture(0)

while(1):
    ret,frame = cap.read()
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
    change(frame,direction)
    cv2.imshow('img',frame)
    if cv2.waitKey(50) & 0xFF == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()
