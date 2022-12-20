from moocxing.package import MOOCXING
from mcpi.minecraft import Minecraft
import cv2
import mcpi.block as block
import time
MX = MOOCXING.INIT()
mc = Minecraft.create()
xclf=cv2.imread('.\\XCLF.jpg')
lcjj=cv2.imread('.\\LCJJ.jpg')
lz=cv2.imread('.\\LZ.jpg')
xcfzj=cv2.imread('.\\XCFRJ.jpg')
xjjy=cv2.imread('.\\XJJY.jpg')
yb=cv2.imread('.\\YB.jpg')
zwy=cv2.imread('.\\ZWY.jpg')
zxt=cv2.imread('.\\ZXT.jpg')
cookerpos = [-129,59,97]
def get_dis():
    mypos = mc.player.getTilePos()
    return (mypos.x-cookerpos[0])**2+(mypos.y-cookerpos[1])**2+(mypos.z-cookerpos[2])**2
def XCLF():
    MX.speech.TTS("香翅捞饭")
    MX.media.play()
    cv2.imshow('frame',xclf)
    cv2.waitKey(1000)
def LCJJ():
    MX.speech.TTS("卤雏鸡脚")
    MX.media.play()
    cv2.imshow('frame',lcjj)
    cv2.waitKey(1000)
def LZ():
    MX.speech.TTS("荔枝")
    MX.media.play()
    cv2.imshow('frame',lz)
    cv2.waitKey(1000)
def XCFRJ():
    MX.speech.TTS("香菜凤仁鸡")
    MX.media.play()
    cv2.imshow('frame',xcfzj)
    cv2.waitKey(1000)
def XJJY():
    MX.speech.TTS("香精煎鱼")
    MX.media.play()
    cv2.imshow('frame',xjjy)
    cv2.waitKey(1000)
def YB():
    MX.speech.TTS("油饼")
    MX.media.play()
    cv2.imshow('frame',yb)
    cv2.waitKey(1000)
def ZWY():
    MX.speech.TTS("蒸乌鱼")
    MX.media.play()
    cv2.imshow('frame',zwy)
    cv2.waitKey(1000)
def ZXT():
    MX.speech.TTS("蒸虾头")
    MX.media.play()
    cv2.imshow('frame',zxt)
    cv2.waitKey(1000)
def recipe():
    MX.speech.TTS("欢迎光临，我们这里有许多菜品，有，香翅捞饭，卤雏鸡脚，荔枝，香菜凤仁鸡，香精煎鱼，油饼，蒸乌鱼，蒸虾头，请问您要来点什么")
    MX.media.play()
def get_speak():
    MX.media.record(RS=6)
    return MX.pinyin.getPinyin(MX.speech.STT())
def CC():
    MX.speech.TTS("您好，这是您要的")
    MX.media.play()
    
while(True):
    time.sleep(3)
    print("going on")
    pos=mc.player.getTilePos()
    mc.postToChat("Your position is x={0} ,y={1} ,z={2}".format(pos.x,pos.y,pos.z))
    if(get_dis()<1000):
        recipe()
        while(True):
            time.sleep(5)
            res = get_speak()
            if(res =='xiangchilaofan。'):
                CC()
                XCLF()
                break
            elif(res =='xiangcaifengrenji。'):
                CC()
                XCFRJ()
                break
            elif(res =='zhenwuyu。' or res =='zhengwuyu。'):
                CC()
                ZWY()
                break
            elif(res =='zhengxiatou。' or res =='zhenxiatou。'):
                CC()
                ZXT()
                break
            elif(res=='luchujijiao。'):
                CC()
                LCJJ()
                break
            elif(res=='lizhi。'):
                CC()
                LZ()
                break
            elif(res=='youbing。'):
                CC()
                YB()
                break
            elif(res=='xiangjinjianyu。'):
                CC()
                XJJY()
                break
            else:
                mc.postToChat("You said {}".format(res))
                print(res)
                MX.speech.TTS("很抱歉没有听清您的需求，请问您要来点什么")
                MX.media.play()
        time.sleep(4)
        cv2.destroyAllWindows()    
    else:
        mc.postToChat("You are too far away from cooker at x=-1041,y=59,z=297,distense is {}".format(get_dis()))
