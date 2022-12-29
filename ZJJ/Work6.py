import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getPos()

def readCsv(filename):
        file=open(filename)
        data = []
    
        while True:       
            line=file.readline().strip()
            if line == "":
                break
            data.append(line.split(","))
    
        file.close()
        return data

class House:
    def __init__(self,name,posx,posy,posz,l,w,h):
        self.name = name
        
        self.posx = posx
        self.posy = posy
        self.posz = posz
        
        self.l = l 
        self.w = w
        self.h = h
    
    def House_Build(self):

        #roof
        for i in range(0,self.w):
            for j in range(0,self.l):
                mc.setBlock(self.posx+i,self.posy+self.h,self.posz+j,block.GLOWSTONE.id)
        
        #wall
        for k in range(1,self.h):
            for i in range(0,self.w):
                if(i == 0 or i == self.w-1):
                    for j in range(0,self.l):
                        if((k==1 or k==2) and (j==4 or j==5)):
                            continue
                        mc.setBlock(self.posx+i,self.posy+k,self.posz+j,block.PURPUR_BLOCK.id)
                else:
                    mc.setBlock(self.posx+i,self.posy+k,self.posz,block.PURPUR_BLOCK.id)
                    mc.setBlock(self.posx+i,self.posy+k,self.posz+self.l-1,block.GLASS.id)          

        #floor
        for i in range(0,self.w):
                for j in range(0,self.l):
                    mc.setBlock(self.posx+i,self.posy,self.posz+j,block.ACACIA_LOG.id)

    def House_isInHouse(self):
        nowpos = mc.player.getPos()
        if (nowpos.x<=self.posx+self.w and nowpos.x>=self.posx) and (nowpos.y<=self.posy+self.l and nowpos.y>=self.posy) and (nowpos.z<=self.posz+self.h and nowpos.z>=self.posz): 
            mc.postToChat("YOU ARE IN THE HOUSE NOW!"+str(self.name))    

pos = mc.player.getPos()
houses = []
for i in range(0,3):
    for j in range(0,3): 
        house = House((i,j),pos.x+i*15,pos.y,pos.z+j*15,10,10,10)
        house.House_Build()
        houses.append(house)
while True:
    for house in houses:
        house.House_isInHouse()
