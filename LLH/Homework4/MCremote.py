import cv2
import mediapipe as mp
import mcpi.minecraft as minecraft
import time
import numpy as np

cap = cv2.VideoCapture(0)

left = cv2.imread("left.jpg",-1)
right = cv2.imread("right.jpg",-1)
up = cv2.imread("up.jpg",-1)
down = cv2.imread("down.jpg",-1)

mc = minecraft.Minecraft.create()

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

x0,y0 = x5,y5 = x8,y8 = 0,0

while True:
    pos = mc.player.getTilePos()
    img= cv2.flip(cap.read()[1],1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)

                if id == 0:
                    x0,y0 = cx,cy

                if id == 5:
                    x5, y5 = cx, cy
                    pos5 = '5' + '(' + str(x5) + ',' + str(y5) + ')'
                    cv2.putText(img, pos5, (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                if id == 8:
                    x8, y8 = cx, cy
                    pos8 = '8' + '(' + str(x8) + ',' + str(y8) + ')'
                    cv2.putText(img, pos8, (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
                
            delta_x = np.abs(x5-x8)
            delta_y = np.abs(y5-y8)
            delta_pos = '(' + str(delta_x) + ',' + str(delta_y) + ')'
            cv2.putText(img, delta_pos, (x0+10, y0+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

            if y5 > y8 and delta_x < delta_y:
                pos.z+=1
                img[0:48,48:96] = up

            if y5 < y8 and delta_x < delta_y:
                pos.z-=1
                img[48:96,48:96] = down

            if x5 < x8 and delta_x > delta_y:
                pos.x-=1
                img[48:96,96:144] = right

            if x5 > x8 and delta_x > delta_y:
                pos.x+=1
                img[48:96,0:48] = left
                    
            mc.player.setTilePos(pos)
            #direction = mc.player.getDirection() #get the player's direction
            #print(direction)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
            
    cv2.imshow("live", img)
    if cv2.waitKey(1000) & 0xFF == 'q':
        break
    #time.sleep(1.0)

cap.release()
cv2.destroyAllWindows()