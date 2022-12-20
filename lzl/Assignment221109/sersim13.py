import serial
import numpy as np
import cv2

face_model = 'haarcascade_frontalface_default.xml'
eye_model = 'haarcascade_eye.xml'
face_cascade = cv2.CascadeClassifier(face_model)
eye_cascade = cv2.CascadeClassifier(eye_model)

ser = serial.Serial("COM13",timeout=1)




offbulb = cv2.imread("bulb-off.png")
onbulb = cv2.imread("bulb-on.png")


def display(img, dir):
    w = img.shape[1]
    h = img.shape[0]
    img[h - 150:h, w // 2 - 50:w // 2 + 50] =offbulb  # up
    img[0:150, w // 2 - 50:w // 2 + 50] =offbulb  # down
    img[h // 2 - 75:h // 2 + 75, 0:100] =offbulb  # left
    img[h // 2 - 75:h // 2 + 75, w - 100:w] =offbulb  # right
    if dir == 'l':
        print("left")
        img[h // 2 - 75:h // 2 + 75, 0:100] = onbulb
    elif dir == 'r':
        print("right")
        img[h // 2 - 75:h // 2 + 75, w - 100:w] = onbulb
    elif dir == 'u':
        print("up")
        img[0:150, w // 2 - 50:w // 2 + 50] = onbulb
    elif dir == 'd':
        print("down")
        img[h - 150:h, w // 2 - 50:w // 2 + 50] = onbulb
    elif dir == 's':
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
