from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

mc.setBlock(pos.x,pos.y,pos.z,1)

stayed_time=0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=58 y=6 z=-103 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==58 and pos.z==-103 and pos.y==6:
        mc.postToChat("welcome home,count down"+str(30-stayed_time))
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(58,26,-103)
            stayed_time=0
    else:
        stayed_time=0
        
