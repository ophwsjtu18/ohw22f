import serial

ser=serial.Serial("COM12")

import numpy as np
import cv2


face_model = 'haarcascade_frontalface_default.xml'
eye_model = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade = cv2.CascadeClassifier(eye_model)


def face2direction(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    width = img.shape[1]
    if len(faces) != 0:
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            mid = x + w / 2
            if mid < width / 3:
                cv2.putText(img, "left", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'LEFT'
            elif mid > 2 * width / 3:
                cv2.putText(img, "right", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'RIGHT'
            elif w > width / 4:
                cv2.putText(img, "top", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'FORWARD'
            elif w < width / 6:
                cv2.putText(img, "down", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'BACKWARD'
            else:
                cv2.putText(img, "standby", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'STANDBY'




while True:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # 如果正确读取帧，ret为True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # 显示结果帧eq
 
    img = cv2.flip(frame,1)
    direction = face2direction(img)
    
    print(direction)
    if direction != None:
        ser.write(direction.encode())
    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    
# while True:
#     a=input("pleas type your cmd here,q for quit, ~ for remote quit :")
#     print(a)
#     if a == 'q':
#         break
#     ser.write(a.encode())

