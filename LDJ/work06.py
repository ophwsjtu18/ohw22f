from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
import random
mc=Minecraft.create()
pos=mc.player.getTilePos()
colorset = [[0,42,57,20],[0,41,20,89],[0,45,35,89]]
names = [["Tom","Jerry","Peter"],["Bob","Lisa","Alice"],["Amy","Tony","Jhon"]]
class Houseset():
    def __init__(self,name,x0,y0,z0,ht=-1,l=10,w=10,h=10):
        self.name = name
        self.a = pos.x+x0
        self.b = pos.y+y0
        self.c = pos.z+z0
        self.wid = w
        self.len = l
        self.high = h
        self.type = ht
    def Housebuild(self):
        hl = max(5,self.len)
        hw = max(5,self.wid)
        hh = max(5,self.high)
        if(self.type==-1):
            th = random.randint(0,2)
        else:
            th = self.type
        #打底
        for i in range(0,hl):
            rd = random.randint(1,2)
            for j in range(0,hw):
                mc.setBlock(self.a+i,self.b,self.c+j,colorset[th][rd])
        #打顶
        for i in range(0,hl):
            rd = random.randint(2,3)
            for j in range(0,hw):
                mc.setBlock(self.a+i,self.b+hh,self.c+j,colorset[th][rd])
        #筑墙
        for i in range(1,hh):
            rd = random.randint(1,2)
            mc.setBlocks(self.a,self.b+i,self.c,self.a+hl-1,self.b+i,self.c+hw-1,colorset[th][rd])
            mc.setBlocks(self.a+1,self.b+i,self.c+1,self.a+hl-2,self.b+i,self.c+hw-2,colorset[th][0])
        #放门
        mc.setBlocks(self.a,self.b+1,self.c+int(hw/2),self.a,self.b+2,self.c+int(hw/2),0)
        #mc.setBlock(self.a,self.b+2,self.c+int(hw/2),block.DOOR_BIRCH.id)

        #放窗
        mc.setBlocks(self.a+int(hl/2),self.b+int(hh/2-2),self.c,self.a+int(hl/2)+2,self.b+int(hh/2),self.c,20)
        mc.setBlocks(self.a+int(hl/2),self.b+int(hh/2-2),self.c+hw-1,self.a+int(hl/2)+2,self.b+int(hh/2),self.c+hw-1,20)
        mc.setBlocks(self.a+hl-1,self.b+int(hh/2-2),self.c+int(hw/2),self.a+hl-1,self.b+int(hh/2),self.c+int(hw/2)+2,20)
    def whetherinhome(self,mypos):
        if (self.a<mypos.x<self.a+self.len and self.c<mypos.z<self.c+self.wid and self.b<mypos.y<self.b+self.high):
            return True
        else:
            return False
    def distense(self,mypos):
        return (self.a-mypos.x)**2+(self.b-mypos.y)**2+(self.c-mypos.z)**2
houseset = []
for i in range(0,3):
    for j in range(0,3):
        house = Houseset(names[i][j],20*i,0,20*j)
        house.Housebuild()
        houseset.append(house)

print("OK")
while(True):
    time.sleep(3)
    print("going on")
    pos=mc.player.getTilePos()
    mc.postToChat("Your position is x={0} ,y={1} ,z={2}".format(pos.x,pos.y,pos.z))
    a = 1
    for house in houseset:
        if(house.whetherinhome(pos)):
            mc.postToChat("Your are in {} 's home".format(house.name))
            a = 0
            break
    if(a==1):
        mindis = houseset[0].distense(pos)
        minhouse = houseset[0]
        for house in houseset:
            if(house.distense(pos)<mindis):
                minhouse = house
                mindis = minhouse.distense(pos)
        mc.postToChat("Your nearest house is {} 's home, at x={},y={},z={}".format(minhouse.name,minhouse.a,minhouse.b,minhouse.c))
