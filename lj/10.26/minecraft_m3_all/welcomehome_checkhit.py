from mcpi.minecraft import Minecraft
import time


#不断检查宝剑右键敲击方块的事件并打印出来，如果在家附近敲击，可以立即飞起

mc=Minecraft.create()
#mc=Minecraft.create("192.168.2.207",4711)

stayed_time=0

while True:
    
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    
    hits=mc.events.pollBlockHits() 
    for hit in hits:
        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z))
        
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home,please wait for 30 rounds for fly")
        mc.postToChat("Or hit something by right click sword, you will fly immediately")
        if len(hits) !=0:
            stayed_time=31
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
    else:
        stayed_time=0
        
     
