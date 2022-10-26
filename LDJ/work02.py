from turtle import shape
import numpy as np
import cv2
img_up = cv2.imread("myopencv\photo_sourse\point_UP.jpg")
img_down = cv2.imread("myopencv\photo_sourse\point_Down.jpg")
img_left = cv2.imread("myopencv\photo_sourse\point_left.jpg")
img_right = cv2.imread("myopencv\photo_sourse\point_right.jpg")
cap = cv2.VideoCapture("myopencv\my_video\CXKGC.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,[2240,1400])
face_cascade = cv2.CascadeClassifier("myopencv\OPENCV_LEARN\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("myopencv\OPENCV_LEARN\haarcascade_eye.xml")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mysize = gray.shape 
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            if(w>400):
                if((x+75<1400)&(y+h+81<2240)):
                    frame[y+h:y+h+81,x:x+75]=img_up
            if(w<100):
                if((x+75+51<1400)&(y+h+54<2240)):
                    frame[y+h:y+h+54,x+75:x+75+51]=img_down
            if(x>700):
                if((x+75+51+56<1400)&(y+h+56<2240)):
                    frame[y+h:y+h+56,x+75+51:x+75+51+56]=img_right
            if(x<700):
                if((x+75+51+52+56<1400)&(y+h+56<2240)):
                    frame[y+h:y+h+54,x+75+51+56:x+75+51+52+56]=img_left
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
 # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
