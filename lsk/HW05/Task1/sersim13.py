import serial
import numpy as np
import cv2

face_model = 'haarcascade_frontalface_default.xml'
eye_model = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade = cv2.CascadeClassifier(eye_model)

ser = serial.Serial("COM13",timeout=1)

darkbulb = cv2.imread("bulb1.png")
lightbulb = cv2.imread("bulb2.png")


def display(img, dir):
    w = img.shape[1]
    h = img.shape[0]
    img[h - 150:h, w // 2 - 50:w // 2 + 50] = darkbulb  # top
    img[0:150, w // 2 - 50:w // 2 + 50] = darkbulb  # down
    img[h // 2 - 75:h // 2 + 75, 0:100] = darkbulb  # left
    img[h // 2 - 75:h // 2 + 75, w - 100:w] = darkbulb  # right
    if dir == 'L':
        print("left")
        img[h // 2 - 75:h // 2 + 75, 0:100] = lightbulb
    elif dir == 'R':
        print("right")
        img[h // 2 - 75:h // 2 + 75, w - 100:w] = lightbulb
    elif dir == 'F':
        print("top")
        img[0:150, w // 2 - 50:w // 2 + 50] = lightbulb
    elif dir == 'B':
        print("down")
        img[h - 150:h, w // 2 - 50:w // 2 + 50] = lightbulb
    elif dir == 'S':
        print("standby")
        return


while True:
    img = cv2.imread("background.png")
    display(img, 'STANDBY')
    print("reading....")
    resp = ser.read()
    if resp != b"":
        a = resp.decode()
        dir = a.strip()
        display(img, dir)
    cv2.imshow('image', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

