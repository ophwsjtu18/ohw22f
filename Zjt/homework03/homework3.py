from asyncio.windows_events import NULL
from enum import Enum
import numpy as np
import cv2
from MXMqtt import MXMqtt
import time
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)

mqtt=MXMqtt("mqtt.16302.com",1883)
mqtt.SUB("ZJT")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

class Direction(Enum):
    left=1
    right=2
    forward=3
    back=4

def Img_Change(img,direction):
    if(direction==None or direction==NULL):
        return
    dirimg = cv2.imread(str(direction.name)+'.png')
    newdirimg = cv2.resize(dirimg,(50,50), interpolation=cv2.INTER_AREA)
    
    w,h,d=img.shape
    wn,hn,dn = newdirimg.shape

    tmp = newdirimg[0:hn,0:wn]
    img[w-wn:w,h-hn:h]=tmp

    return

def Face_Recognition(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)


    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return faces

def Mc_Build(pos = None):
    if pos is None:
        position = mc.player.getTilePos()
    else:
        position = pos 
    for i in range(0,13*2):#hang
        for j in range(0,13*2):#lie
            if(i!=13):
                mc.setBlock(position.x+13,position.y+i,position.z,block.STONE.id)
                break
            else:
                mc.setBlock(position.x+j,position.y+i,position.z,block.STONE.id)
    return position

def Face_Direction(shape,faces):
    if(len(faces)==0):
        return
    
    height,width,deepth = shape
    
    leftLimit = width/3
    rightLimit = width*2/3

    maxLimitW = width/1.5
    maxLimitH = height/1.5

    minLimitW = width/2.5
    minLimitH = height/2.5

    direction = NULL
    for (x,y,w,h) in faces:
        horLocation=x+w/2
        if(horLocation<leftLimit):
            print("left")
            direction = Direction.left
        elif(horLocation>rightLimit):
            print("right")
            direction = Direction.right
        elif(w>maxLimitW or h>maxLimitH):
            mc.postToChat("forward")
            direction = Direction.forward
        elif(w<minLimitW or h<minLimitH): 
            print("back")
            direction = Direction.back
        else:
            print("stanndBy")

        mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    return direction

def Led_lightmove(position,direction):
    if(direction == None or direction == NULL):
        mqtt.PUB("ZJT","STAND_BY")
        Mc_Build(position)
        return

    pos=mc.player.getTilePos()
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    if direction.name == "left":
        mqtt.PUB("ZJT","LEFT")
        mc.setBlock(position.x+25,position.y+13,position.z,block.DIAMOND_BLOCK.id)
        mc.postToChat("left")
        pos.x+=1

    elif direction.name == "right":
        mqtt.PUB("ZJT","RIGHT")
        mc.setBlock(position.x+0,position.y+13,position.z,block.DIAMOND_BLOCK.id)
        mc.postToChat("right")
        pos.x-=1

    elif direction.name == "forward":
        mqtt.PUB("ZJT","TOP")
        mc.setBlock(position.x+13,position.y+25,position.z,block.DIAMOND_BLOCK.id)
        print("forward")
        pos.z+=1

    elif direction.name == "back":
        mqtt.PUB("ZJT","DOWN")
        mc.setBlock(position.x+13,position.y+0,position.z,block.DIAMOND_BLOCK.id)
        mc.postToChat("back")
        pos.z-=1

    #mc.player.setTilePos(pos) 

cap = cv2.VideoCapture(0)

position=Mc_Build()
while(True):
    
    ret,frame = cap.read()
    
    #frame = cv2.flip(frame,1)
    #frame = cv2.flip(frame,0)
    imgshape=frame.shape
    faces=Face_Recognition(frame)
    direction = Face_Direction(imgshape,faces)
    Led_lightmove(position,direction)
    Img_Change(frame,direction)

    cv2.imshow('img',frame)
    if cv2.waitKey(25) & 0xFF == ord('1'):
        break

cap.release()
cv2.destroyAllWindows()