import cv2
import mediapipe as mp
from math import sqrt 
from mcpi.minecraft import Minecraft
from enum import Enum
from asyncio.windows_events import NULL

class Direction(Enum):
    left=1
    right=2
    forward=3
    back=4

def getDis(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

def getCmd(x,y):
    #8
    dis1 = getDis(x[2],y[2],x[8],y[8])
    #12
    dis2 = getDis(x[2],y[2],x[12],y[12])
    #16
    dis3 = getDis(x[2],y[2],x[16],y[16])
    #20
    dis4 = getDis(x[2],y[2],x[20],y[20])

    direction = NULL

    if(dis1 > 100 and dis2 < 100 and dis3 < 100 and dis4 < 100):
        print('forward')
        direction = Direction.forward
    if(dis1 > 100 and dis2 > 100 and dis3 < 100 and dis4 < 100):
        print('back')
        direction = Direction.back
    if(dis1 > 100 and dis2 > 100 and dis3 > 100 and dis4 < 100):
        print('left')
        direction = Direction.left
    if(dis1 > 100 and dis2 > 100 and dis3 > 100 and dis4 > 100):
        print('right')
        direction = Direction.right
    return direction

def Mc_Move(direction):
    if(direction == NULL):
        return

    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    if direction.name == "left":
        mc.postToChat("left")
        pos.x+=1

    elif direction.name == "right":
        mc.postToChat("right")
        pos.x-=1

    elif direction.name == "forward":
        mc.postToChat("forward")
        pos.z+=1

    elif direction.name == "back":
        mc.postToChat("back")
        pos.z-=1

    mc.player.setTilePos(pos) 

x1= {}
y1 = {}


mc=Minecraft.create()
pos=mc.player.getTilePos()

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    img= cv2.flip(cap.read()[1],1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                x1[id] = cx
                y1[id] = cy
                cv2.putText(img, str(int(id)), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        dir = getCmd(x1,y1)
        Mc_Move(dir)
    cv2.imshow("image", img)
    if cv2.waitKey(2) & 0xFF == 27:
        break

cap.release()    
cv2.destroyAllWindows()