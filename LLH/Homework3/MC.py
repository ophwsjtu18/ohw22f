import mcpi.minecraft as minecraft
import mcpi.block as block
from MXMqtt import MXMqtt
import numpy as np
import cv2
import time

#mqtt = MXMqtt("mqtt.16302.com",1883)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

mc.setBlock(pos.x, pos.y, pos.z+5, block.STONE.id)
mc.setBlock(pos.x, pos.y+1, pos.z+5, block.STONE.id)
mc.setBlock(pos.x, pos.y+2, pos.z+5, block.STONE.id)
mc.setBlock(pos.x, pos.y+3, pos.z+5, block.STONE.id)
mc.setBlock(pos.x+1, pos.y+2, pos.z+5, block.STONE.id)
mc.setBlock(pos.x-1, pos.y+2, pos.z+5, block.STONE.id)  #bulid basic cross

while(True):
    time.sleep(0.1)
    
    mc.setBlock(pos.x, pos.y, pos.z+5, block.STONE.id)
    mc.setBlock(pos.x, pos.y+1, pos.z+5, block.STONE.id)
    mc.setBlock(pos.x, pos.y+2, pos.z+5, block.STONE.id)
    mc.setBlock(pos.x, pos.y+3, pos.z+5, block.STONE.id)
    mc.setBlock(pos.x+1, pos.y+2, pos.z+5, block.STONE.id)
    mc.setBlock(pos.x-1, pos.y+2, pos.z+5, block.STONE.id)    #refresh sign

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    size = img.shape
    midy = int(size[0]/2)
    midx = int(size[1]/2)
    if(midx>midy):
        sizec = size[0]
    else:
        sizec = size[1]

    font = cv2.FONT_HERSHEY_SIMPLEX
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        midfx = int(x+w/2)
        midfy = int(y+h/2)

        if(np.abs(midfx-midx)<20 & np.abs(midfy-midy)<20):
            cv2.putText(img,"center",(x,y),font,0.5,(0,255,0),1)
            mc.setBlock(pos.x, pos.y+2, pos.z+5, block.GLASS.id)
            #mc.postToChat("center")
           # mqtt.PUB("LLH","STAND_BY")

        elif(midfx<midx):
            cv2.putText(img,"left",(x,y),font,0.5,(0,255,0),1)
            mc.setBlock(pos.x+1, pos.y+2, pos.z+5, block.GLASS.id)
            #mc.postToChat("left")
           # mqtt.PUB("LLH","LEFT")
            
        elif(midfx>midx):
            cv2.putText(img,"right",(x,y),font,0.5,(0,255,0),1)
            mc.setBlock(pos.x-1, pos.y+2, pos.z+5, block.GLASS.id)
            #mc.postToChat("right")
            #mqtt.PUB("LLH","RIGHT")
            
        elif(midfy<midy):
            cv2.putText(img,"top",(x,y+13),font,0.5,(0,255,0),1)
            mc.setBlock(pos.x, pos.y+3, pos.z+5, block.GLASS.id)
            #mc.postToChat("top")
            #mqtt.PUB("LLH","TOP")

        elif(midfy>midy):
            cv2.putText(img,"down",(x,y+13),font,0.5,(0,255,0),1)
            mc.setBlock(pos.x, pos.y+1, pos.z+5, block.GLASS.id)
            #mc.postToChat("down")
            #mqtt.PUB("LLH","DOWN")

    cv2.imshow('live',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()