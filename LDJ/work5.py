'''input.py'''
import numpy as np
import cv2
import serial
ser=serial.Serial("COM12")
a = ""
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("OPENCV_LEARN\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("OPENCV_LEARN\haarcascade_eye.xml")
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
            a=""
            dx = x+w/2-mysize[0]/2
            if(w>250):
                a= "up"
            elif(w<150) :
                a = "down"
            elif(dx>=50):
                a = "right"
            elif(dx<=-50):
                a = "left"
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.imshow('frame',frame)
        ser.write(a.encode())
        print(a)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            a = 'end'
            ser.write(a.encode())
            break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows() 

'''output.py''' 

import serial
import cv2
import time
import numpy as np
light = cv2.imread("photo_sourse\light.jpg")
background = cv2.imread("photo_sourse\WHITE.jpg")
ser=serial.Serial("COM13",timeout=1)
img0 = background
img1 = background.copy()
img1[0:240,200:440]=light
img2 = background.copy()
img2[240:480,200:440]=light
img3 = background.copy()
img3[120:360,0:240]=light
img4 = background.copy()
img4[120:360,400:640]=light
myimg = [img0,img1,img2,img3,img4]
def mydecode(str):
    i=0
    while(i<=10):
        if(str[i]=='u'):
            return 'up'
        elif(str[i]=='d'):
            return 'down'
        elif(str[i]=='l'):
            return 'left'
        elif(str[i]=='r'):
            return 'right'
        else:
            i+=1
    return " "
while True:
    print("reading....")
    resp=ser.read(11)
    which = 0
    if resp != b"":
        a=resp.decode()
        print(a)
        if(a=="~"):
            break
        print("get commnd, I will handle it",a)
        if(mydecode(a)=='up'):
            which = 1
        elif(mydecode(a)=='down'):
            which = 2
        elif(mydecode(a)=='left'):
            which =3
        elif(mydecode(a)=='right'):
            which = 4
        elif(mydecode(a)==" "):
            which = 0
        elif(mydecode(a)=='end'):
            break
    else:
        print("working on something else..")
    cv2.imshow("frame",myimg[which])
    cv2.waitKey(100)
cv2.destroyAllWindows()
