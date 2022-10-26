from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f=open("block.csv",'w')
L=20
W=20
H=15
for y in range (H):
    for x in range (L):
        for z in range (W):
            block=mc.getBlockWithData(pos.x+x+1,pos.y+y,pos.z+z+1)
            f.write(str(block.id))
            f.write('|')
            f.write(str(block.data))
            if z < W-1:
                f.write(',')

        f.write('\n')
        print(x,y)
f.close()
