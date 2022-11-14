import serial
import cv2
import numpy as np
ser=serial.Serial("COM13",timeout=1)

light = cv2.imread('./light.png')
img = np.ones((1200, 1200, 3), dtype=np.uint8)
img *= 255 # white background

left = img[0:356,350:700]
cv2.imshow('image',light)
while True:
    print("reading....")
    resp=ser.readline()
    # print(resp)
    if resp != b"":
        a=resp.decode()
        b=a.strip()
        if b == 'LEFT':
            left = light
            cv2.imshow('image',img)
            cv2.waitKey(100)
            print(111)
        if b == '~':
            break
    else:
        print("working on something else..")    
# while True:
#     print("reading....")
#     resp=ser.readline()
#     if resp != b"":
#         a=resp.decode()
#         print(a)
#         print("get commnd, I will handle it",resp)
#         b=a.strip()
#         if b == '~':
#             break
#         c=b.split(",")
#         d=list(map(int,c))
#         servo1=d[0]
#         servo2=d[1]
#         servo3=d[2]
#         print("move servo to angle",servo1,servo2,servo3)
#     else:
#         print("working on something else..")
    
