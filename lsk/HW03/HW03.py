import numpy as np
import cv2
from MXMqtt import MXMqtt
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

mqtt = MXMqtt("mqtt.16302.com", 1883)

face_model = 'haarcascade_frontalface_default.xml'
eye_model = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade = cv2.CascadeClassifier(eye_model)

LEFT = 1
RIGHT = 2
FORWARD = 3
BACKWARD = 4
STANDBY = 5


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
                return LEFT
            elif mid > 2 * width / 3:
                cv2.putText(img, "right", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return RIGHT
            elif w > width / 4:
                cv2.putText(img, "top", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return FORWARD
            elif w < width / 6:
                cv2.putText(img, "down", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return BACKWARD
            else:
                cv2.putText(img, "standby", (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                return STANDBY


def display(dir):
    if dir == LEFT:
        mqtt.PUB("LSK", "LEFT")
        mc.setBlock(-99, 0, 2, 57)
        mc.setBlock(-101, 0, 2, 4)
        for j in range(1, 3):
            mc.setBlock(-100, 0, j, 4)
        return
    elif dir == RIGHT:
        mqtt.PUB("LSK", "RIGHT")
        mc.setBlock(-101, 0, 2, 57)
        mc.setBlock(-99, 0, 2, 4)
        for j in range(1, 3):
            mc.setBlock(-100, 0, j, 4)
        return
    elif dir == FORWARD:
        mqtt.PUB("LSK", "TOP")
        mc.setBlock(-100, 0, 3, 57)
        mc.setBlock(-100, 0, 1, 4)
        for i in range(-101, -99):
            mc.setBlock(i, 0, 2, 4)
        return
    elif dir == BACKWARD:
        mqtt.PUB("LSK", "DOWN")
        mc.setBlock(-100, 0, 1, 57)
        mc.setBlock(-100, 0, 3, 4)
        for i in range(-101, -99):
            mc.setBlock(i, 0, 2, 4)
        return
    elif dir == STANDBY:
        mqtt.PUB("LSK", "STAND_BY")
        for i in range(-101, -99):
            mc.setBlock(i, 0, 2, 4)
        for j in range(1, 3):
            mc.setBlock(-100, 0, j, 4)
        return


cap = cv2.VideoCapture(1)
while True:

    ret, frame = cap.read()
    img = cv2.flip(frame, 1)
    direction = face2direction(img)
    display(direction)
    cv2.imshow('frame', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
