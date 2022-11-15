import serial
import numpy as np
import cv2

face_model = 'haarcascade_frontalface_default.xml'
eye_model = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade = cv2.CascadeClassifier(eye_model)

ser = serial.Serial("COM12")


def face2direction(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    width = img.shape[1]
    if len(faces) != 0:
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            mid = x + w / 2
            if mid < width / 3:
                print("left")
                cv2.putText(img, "left", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'L'
            elif mid > 2 * width / 3:
                print("right")
                cv2.putText(img, "right", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'R'
            elif w > width / 4:
                print("top")
                cv2.putText(img, "top", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'F'
            elif w < width / 6:
                print("down")
                cv2.putText(img, "down", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return 'B'
            else:
                print("standby")
                return 'S'


cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    img = cv2.flip(frame, 1)
    dir = face2direction(img)
    cv2.imshow('frame', img)
    if dir is not None:
        ser.write(dir.encode())
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
