from mcpi.minecraft import Minecraft
import mcpi.block as block
import time

mc=Minecraft.create()

f = open("cross.csv")
roof = []
while True:
    line = f.readline().strip()
    if line == '':
        break
    roof.append(line.split(","))

f = open("floor.csv")
floor = []
while True:
    line = f.readline().strip()
    if line == '':
        break
    floor.append(line.split(","))


pos=mc.player.getTilePos()
print("player pos is",pos)

class House():
    def __init__(self,name,x0,y0,z0,l,w,h):
        self.name=name
        self.x0=x0+1
        self.y0=y0+1
        self.z0=z0+1
        self.l = l
        self.w = w
        self.h = h
        print("I will build a house named",self.name)

    def build(self):
        print("I will buildwall on",self.x0,self.y0,self.z0)
        for i in range(self.l):
            for j in range(self.w):
                if roof[i][j] == '0':
                    mc.setBlock(self.x0+i, self.y0+self.h, self.z0+j, block.GLASS.id)
                else:
                    mc.setBlock(self.x0+i, self.y0+self.h, self.z0+j, block.GLOWSTONE_BLOCK.id)

        for i in range(self.l):
            for j in range(self.w):
                if floor[i][j] == '0':
                    mc.setBlock(self.x0+i, self.y0, self.z0+j, block.WOOD.id)
                else:
                    mc.setBlock(self.x0+i, self.y0, self.z0+j, block.GOLD_BLOCK.id)

        for i in range(1,self.h):
            for k in range(self.w):
                if k == 0 or k == self.w-1:
                    for j in range(self.l):
                        mc.setBlock(self.x0+j, self.y0+i, self.z0+k, block.GLASS.id)
                elif k != int(self.w/2) or i>=4:
                    mc.setBlock(self.x0, self.y0+i, self.z0+k, block.GLASS.id)
                    mc.setBlock(self.x0+self.l-1, self.y0+i, self.z0+k, block.GLASS.id)

    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+self.l and self.z0<z1<self.z0+self.w and self.y0<y1<self.y0+self.h:
            return True
        else:
            return False
        
houses=[]
name = ['Peter','Alice','Remon','Lancy','Steven','Ciara','Sandy','Lona','Davy']
distance = 10
l = 5
w = 7
h = 10

for i in range(9):
    houses.append(House(name[i],pos.x+distance*(i%3) ,pos.y, pos.z+distance*(i//3),l,w,h))
    print("house"+str(i)+" name is",houses[i].name)
    houses[i].build()

while True:
    flag = True
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    for house in houses:
        if house.isInHome(pos.x,pos.y,pos.z):
            print("Welcome to "+ house.name +" home")
            flag = False
    if flag:
        print("You are outside")

