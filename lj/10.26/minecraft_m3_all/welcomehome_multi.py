from mcpi.minecraft import Minecraft
from mcpi.minecraft import CmdPositioner
import time

mc=Minecraft.create("192.168.3.199",4711)

players=mc.getPlayerEntityIds()
print("player ids is",players)

try:
    playername="xkn"
    pid=mc.getPlayerEntityId(playername)
    print(playername," pid is ",pid)
    cp=CmdPositioner(mc.conn,b"player")
    pos=cp.getTilePos(pid)
    print("player pos ",pos)
except:
    print("player ", playername," not found")
    exit()

stayed_time=0
while True:
    time.sleep(2)
    pos=cp.getTilePos(pid)
    mc.postToChat(playername+" x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
 
        
     
