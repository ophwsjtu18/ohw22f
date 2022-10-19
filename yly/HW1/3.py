import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
X=cap.get(3)
Y=cap.get(4)
pic1=cv2.imread('1.jpg',0)
pic2=cv2.imread('2.jpg',0)
pic3=cv2.imread('3.jpg',0)
while(True):
    ret,frame = cap.read()
    frame=cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img=frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if x+w<X/2:
            print("left")
            cv2.imshow('pic',cv2.flip(pic1,1))
        else:
            if x>X/2:
                print("right")
                cv2.imshow('pic',pic1)
            else:
                if h>Y/4*3:
                    print("forward")
                    cv2.imshow('pic',pic2)
                else:
                    if h<Y/3:
                        print("backward")
                        cv2.imshow('pic',cv2.flip(pic2,1))
                    else:
                        print("stand by")
                        cv2.imshow('pic',pic3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
