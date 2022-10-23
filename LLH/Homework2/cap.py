import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
left = cv2.imread("left.jpg",-1)
right = cv2.imread("right.jpg",-1)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    size = img.shape
    midy = int(size[0]/2)
    midx = int(size[1]/2)
    if(midx>midy):
        sizec = size[0]
    else:
        sizec = size[1]

    font = cv2.FONT_HERSHEY_SIMPLEX
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        midfx = int(x+w/2)
        midfy = int(y+h/2)

        if(np.abs(midfx-midx)<20):
            cv2.putText(img,"center",(x,y),font,0.5,(0,255,0),1)
        elif(midfx<midx):
            cv2.putText(img,"left",(x,y),font,0.5,(0,255,0),1)
            img[0:48,0:48] = left
        elif(midfx>midx):
            cv2.putText(img,"right",(x,y),font,0.5,(0,255,0),1)
            img[0:48,0:48] = right
        
        if((sizec*sizec)/(w*h)>9):
            cv2.putText(img,"backword",(x,y+13),font,0.5,(0,255,0),1)
        elif((sizec*sizec)/(w*h)<5):
            cv2.putText(img,"forword",(x,y+13),font,0.5,(0,255,0),1)
    cv2.imshow('live',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()