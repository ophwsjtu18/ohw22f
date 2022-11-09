import numpy as np
import cv2
import serial

ser=serial.Serial("COM1",timeout=1)

led_on = cv2.imread('led_on.png')
led_off = cv2.imread('led_off.png')

background = cv2.imread('background.png')

def LED_OffAll(img):
    img[200:625,0:300] = led_off;
    img[200:625,944:1244] = led_off;

    img[0:425,500:800] = led_off;
    img[275:700,500:800] = led_off;

def LED_Light(img,direction):
    if not (direction == 'forward' or direction == 'back' or direction == 'right' or direction == 'left'):
        return
    LED_OffAll(img)
    if direction == 'forward':
        background[0:425,500:800] = led_on;
        print('forward')
    if direction == 'back':
        background[275:700,500:800] = led_on;
        print('back')
    if direction == 'right':
        background[200:625,944:1244] = led_on;
        print('right')
    if direction == 'left': 
        background[200:625,0:300] = led_on;
        print('left')
background[200:625,0:300] = led_off;
background[200:625,944:1244] = led_off;

background[0:425,500:800] = led_off;
background[275:700,500:800] = led_off;

while True:
    resp=ser.readline()
    if resp != b"":
        direction = resp.decode().strip()
        print(direction)
        LED_Light(background,direction)

    cv2.imshow('background',background);
    if cv2.waitKey(50) & 0xFF == ord('1'):
        break;
cv2.destroyAllWindows()