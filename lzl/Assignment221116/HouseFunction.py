from mcpi.minecraft import Minecraft

mc = Minecraft.create()

pos = mc.player.getTilePos()
print("player pos is", pos)


class House():
    def __init__(self, name, x0, y0, z0, l, w, h):
        self.name = name
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.l = l
        self.w = w
        self.h = h
        print("I will build a house named ", self.name)

    def buildWall(self, a):
        mc.setBlocks(self.x0, self.y0 + 1, self.z0, self.x0 + self.l - 1, self.y0 + self.h - 1, self.z0 + self.w - 1, a)
        mc.setBlocks(self.x0 + 1, self.y0 + 1, self.z0 + 1, self.x0 + self.l - 2, self.y0 + self.h - 1,
                     self.z0 + self.w - 2, 0)

    def buildRoof(self, a, b):
        f1 = open("roof.csv")
        roof = []
        while True:
            line1 = f1.readline().strip()
            if line1 == "":
                break
            roof.append(line1.split(","))
        for i in range(self.l):
            for j in range(self.w):
                if roof[i][j] == '0':
                    mc.setBlock(self.x0 + i, self.y0 + self.h, self.z0 + j, a)
                elif roof[i][j] == '1':
                    mc.setBlock(self.x0 + i, self.y0 + self.h, self.z0 + j, b)

    def buildFloor(self, a, b):
        f2 = open("floor.csv")
        floor = []
        while True:
            line2 = f2.readline().strip()
            if line2 == "":
                break
            floor.append(line2.split(","))
        for i in range(self.l):
            for j in range(self.w):
                if floor[i][j] == '0':
                    mc.setBlock(self.x0 + i, self.y0, self.z0 + j, a)
                elif floor[i][j] == '1':
                    mc.setBlock(self.x0 + i, self.y0, self.z0 + j, b)

    def isInHome(self, x1, y1, z1):
        if self.x0 < x1 < self.x0 + self.l and self.y0 < y1 < self.y0 + self.h and self.z0 < z1 < self.z0 + self.w:
            return True
        else:
            return False


houses = []
house1 = House("Peter's", pos.x, pos.y, pos.z, 10, 10, 8)
house2 = House("Tom's", pos.x, pos.y, pos.z + 20, 10, 10, 10)
house3 = House("Gyq's", pos.x, pos.y, pos.z + 40, 10, 10, 8)
house4 = House("Kiki's", pos.x + 20, pos.y, pos.z, 10, 10, 8)
house5 = House("Qiqi's", pos.x + 20, pos.y, pos.z + 20, 10, 10, 15)
house6 = House("Qubao's", pos.x + 20, pos.y, pos.z + 40, 10, 10, 10)
house7 = House("GuoYongqi's", pos.x + 40, pos.y, pos.z, 10, 10, 11)
house8 = House("Ququ's", pos.x + 40, pos.y, pos.z + 20, 10, 10, 15)
house9 = House("Hahabao's", pos.x + 40, pos.y, pos.z + 40, 10, 10, 10)

houses.append(house1)
houses.append(house2)
houses.append(house3)
houses.append(house4)
houses.append(house5)
houses.append(house6)
houses.append(house7)
houses.append(house8)
houses.append(house9)

house1.buildWall(1)
house2.buildWall(3)
house3.buildWall(4)
house4.buildWall(41)
house5.buildWall(42)
house6.buildWall(45)
house7.buildWall(49)
house8.buildWall(57)
house9.buildWall(20)

house1.buildRoof(20, 1)
house2.buildRoof(20, 3)
house3.buildRoof(20, 4)
house4.buildRoof(20, 41)
house5.buildRoof(20, 42)
house6.buildRoof(20, 45)
house7.buildRoof(20, 49)
house8.buildRoof(20, 57)
house9.buildRoof(20, 20)

house1.buildFloor(35, 1)
house2.buildFloor(35, 3)
house3.buildFloor(35, 4)
house4.buildFloor(35, 41)
house5.buildFloor(35, 42)
house6.buildFloor(35, 45)
house7.buildFloor(35, 49)
house8.buildFloor(35, 57)
house9.buildFloor(35, 20)

while True:
    pos = mc.player.getTilePos()
    for house in houses:
        if house.isInHome(pos.x, pos.y, pos.z):
            mc.postToChat("Welcome to " + house.name + " home")