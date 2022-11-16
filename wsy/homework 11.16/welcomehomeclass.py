from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

pos=mc.player.getTilePos()
print("player pos is",pos)

def buildHouse(x0,y0,z0):
    #Build wall
    for y in range(6):
        if y%2==0:
            m=57
        else:   
            m=35
        for x in range(10): 
            mc.setBlock(x0+x,y0+y,z0,m)
            mc.setBlock(x0+x,y0+y,z0+15,m)
        for z in range(15):
            mc.setBlock(x0,y0+y,z0+z,m)
            mc.setBlock(x0+10,y0+y,z0+z,m)
    #Build floor in wool
    for x in range(10):
        for z in range(15):
            mc.setBlock(x0+x,y0,z0+z,35,2)

    #Build roof in glass
    for x in range(10):
        for z in range(15):
            mc.setBlock(x0+x,y0+6,z0+z,20)

    #Build door in the middle of x
    mc.setBlock(x0+5,y0+1,z0,0)
    mc.setBlock(x0+5,y0+2,z0,0)

    #Build window in the middle of z
    mc.setBlock(x0+10,y0+3,z0+7,20)
    mc.setBlock(x0+10,y0+4,z0+7,20)
    mc.setBlock(x0+10,y0+3,z0+8,20)
    mc.setBlock(x0+10,y0+4,z0+8,20)

class House():
    def __init__(self,name,x0,y0,z0):
        self.name=name
        self.x0=x0
        self.y0=y0
        self.z0=z0
        print("I will build a house named",self.name)
    def buildWall(self):
        print("I will buildwall on",self.x0,self.y0,self.z0)
        #please add your real block seting code here
        # for.........
        #   mc.setBlock........
    #build roof add your code here
    #build floor add your code here
        buildHouse(self.x0,self.y0,self.z0)

        
    def isInHome(self,x1,y1,z1):
        if self.x0<x1<self.x0+10 and self.z0<z1<self.z0+10:
            return True
        else:
            return False
        
houses=[]
house1=House("peter",pos.x,pos.y,pos.z)
house2=House("guagua",pos.x+20,pos.y,pos.z)
house3=House("huahua",pos.x+40,pos.y,pos.z)
house4=House("xuyi",pos.x,pos.y,pos.z+20)
house5=House("xibao",pos.x+20,pos.y,pos.z+20)
house6=House("enbao",pos.x+40,pos.y,pos.z+20)
house7=House("chenbao",pos.x,pos.y,pos.z+40)
house8=House("tianshuo",pos.x+20,pos.y,pos.z+40)
house9=House("ruizhi",pos.x+40,pos.y,pos.z+40)
houses.append(house1)
houses.append(house2)
houses.append(house3)
houses.append(house4)
houses.append(house5)
houses.append(house6)
houses.append(house7)
houses.append(house8)
houses.append(house9)
house1.buildWall()
house2.buildWall()
house3.buildWall()
house4.buildWall()
house5.buildWall()
house6.buildWall()
house7.buildWall()
house8.buildWall()
house9.buildWall()
print("house1 name is",house1.name)
print("house2 name is",house2.name)

#house1.buildWall()
#house2.buildWall()





'''
buildHouse(pos.x,pos.y,pos.z,10,10,15)
buildHouse(pos.x+20,pos.y,pos.z,10,10,15)
buildHouse(pos.x+40,pos.y,pos.z,10,10,15)
'''
stayed_time=0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    for house in houses:
        if house.isInHome(pos.x,pos.y,pos.z):
            print("Welcome to "+house.name+" home")
    if pos.x==-30 and pos.z==-40 and pos.y==-6:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(-32,9,-45)
            stayed_time=0
    else:
        stayed_time=0
    
     
