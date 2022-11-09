import cv2
import pyautogui as ui
import numpy as np
from mcpi.minecraft import Minecraft
import mediapipe as mp
from math import sqrt 
cap = cv2.VideoCapture(0)
mc=Minecraft.create()
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
def getDis(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)
x5,y5=0,0
x8,y8=0,0
x9,y9=200,0
x11,y11=0,200
while True:
    ret , frame = cap.read()
    img= cv2.flip(frame,1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x*frame_width), int(lm.y*frame_height)
                if(id==9):
                    x9,y9=cx,cy
                if(id==5):
                    x5,y5=cx,cy
                if(id==8):
                    x8,y8=cx,cy
                if(id==11):
                    x11,y11=cx,cy
                if(getDis(x9,y9,x11,y11)<=50):
                    if(getDis(x5,y5,x8,y8)>60):
                        dx=0
                        dy=0
                        if(abs(x8-x5)>10):
                            if(x8>x5):
                                dx = 1
                            else:
                                dx =-1
                        if(abs(y8-y5)>10):
                            if(y8>y5):
                                dy=1
                            else:
                                dy=-1
                        mydir=mc.player.getTilePos()
                        mc.player.setTilePos([mydir.x+dx,mydir.y,mydir.z+dy])
                        
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("image", img)
    if cv2.waitKey(2) & 0xFF == 27:
        break
cap.release()
