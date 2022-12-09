from moocxing.package import MOOCXING
from bs4 import BeautifulSoup
import cv2
import time
import markdown
import sound
import os
import shutil

dish_address = ".\\HowToCook\\dishes\\"
dish_folder = ['aquatic', 'breakfast', 'condiment', 'dessert', 'drink', 'meat_dish', 'semi-finished', 'soup', 'staple', 'template', 'vegetable_dish']

class Robot:
    def __init__(self):
        self.mx = MOOCXING.INIT()
        self.brain = MOOCXING.BRAIN()
 
    def recordS2T(self):
        sound.Sound_Get("speech.wav")
        return sound.Sound_S2T("speech.wav")

    def T2Splay(self,text):
        if sound.Sound_T2S(text,"feedback"):
            sound.Sound_Play("feedback")
            return True
        else:
            return False
    def readM2T(self,filename):
        txt = ""
        
        with open(filename,'r',encoding = "UTF-8") as file:
            for line in file.readlines():
                html = markdown.markdown(line)
                soup = BeautifulSoup(html, features='html.parser')
                txt = txt + soup.get_text()
        file.close()

        return txt

    def getFoodName(self,text):
        return self.mx.nlp.getFoodName(text)

    def findFood(self,order):
        for dish in dish_folder:
            mdname = ""
            jpgname = ""
            if order in os.listdir(dish_address+dish):
                mdname = dish_address+dish+"\\"+order+"\\"+order+".md"
                if order + ".jpg" in os.listdir(dish_address+dish + "\\" + order):
                    jpgname = dish_address+dish+"\\"+order+"\\"+order+".jpg"
                return mdname,jpgname
    
#print(str(dish_folder[1]))
robot = Robot()
'''
for li in range(len(dish_folder)):
    print(os.listdir(dish_address+dish_folder[li]))
    for folder in os.listdir(dish_address+dish_folder[li]):
        for file in os.listdir(dish_address+dish_folder[li]+"\\"+folder):
            print(file)
            if ".md" in file:
                os.renames(dish_address+dish_folder[li]+"\\"+folder+"\\"+file,dish_address+dish_folder[li]+"\\"+folder+"\\"+robot.mx.pinyin.getPinyin(file.replace(".md",""))+".md")
            elif ".jpg" in file:
                os.renames(dish_address+dish_folder[li]+"\\"+folder+"\\"+file,dish_address+dish_folder[li]+"\\"+folder+"\\"+robot.mx.pinyin.getPinyin(file.replace(".jpg",""))+".jpg")
        os.renames(dish_address+dish_folder[li]+"\\"+folder,dish_address+dish_folder[li]+"\\"+robot.mx.pinyin.getPinyin(folder))
'''
robot.mx.minecraft.postToChat("robot start")
while True:
    result = robot.recordS2T()
    order0 = robot.getFoodName(result)
    order = robot.mx.pinyin.getPinyin(order0)
    md,jpg = robot.findFood(order)
    
    if jpg !="":
        try:
            img = cv2.imread(jpg)
            cv2.imshow(order,img)
            cv2.waitKey(0)
        except Exception as e:
            print(e)
            cv2.destroyAllWindows()

    if md != "":
        txt = robot.readM2T(md)
        #robot.mx.minecraft.postToChat(txt)
        if not robot.T2Splay(txt):
            print(txt)
        
        content = "好的，我这就去做"+order0
        robot.mx.minecraft.postToChat(content)
        print(content)



