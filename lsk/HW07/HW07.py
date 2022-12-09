from moocxing.package import MOOCXING
from mcpi.minecraft import Minecraft
import cv2
import mcpi.block as block
import time

MX = MOOCXING.INIT()
mc = Minecraft.create()

cookerpos = [423, 56, 113]
gbjd = cv2.imread("C:\Users\86158\Desktop\PythonProject\HW07\photos\gbjd.jpg")
hsr = cv2.imread("C:\Users\86158\Desktop\PythonProject\HW07\photos\hsr.jpg")
ksbc = cv2.imread("C:\Users\86158\Desktop\PythonProject\HW07\photos\ksbc.jpg")
mpdf = cv2.imread("C:\Users\86158\Desktop\PythonProject\HW07\photos\mpdf.jpg")
ssy = cv2.imread("C:\Users\86158\Desktop\PythonProject\HW07\photos\ssy.jpg")

def get_dis():
    mypos = mc.player.getTilePos()
    return (mypos.x - cookerpos[0]) ** 2 + (mypos.y - cookerpos[1]) ** 2 + (mypos.z - cookerpos[2]) ** 2


def GBJD():
    MX.speech.TTS("宫保鸡丁")
    MX.media.play()
    cv2.imshow('frame', gbjd)
    cv2.waitKey(1000)


def HSR():
    MX.speech.TTS("红烧肉")
    MX.media.play()
    cv2.imshow('frame', hsr)
    cv2.waitKey(1000)


def KSBC():
    MX.speech.TTS("开水白菜")
    MX.media.play()
    cv2.imshow('frame', ksbc)
    cv2.waitKey(1000)


def MPDF():
    MX.speech.TTS("麻婆豆腐")
    MX.media.play()
    cv2.imshow('frame', mpdf)
    cv2.waitKey(1000)


def SSY():
    MX.speech.TTS("松鼠鱼")
    MX.media.play()
    cv2.imshow('frame', ssy)
    cv2.waitKey(1000)


def menu():
    MX.speech.TTS(
        "欢迎光临，我们这里有许多菜品，有，宫保鸡丁，红烧肉，开水白瓷，麻婆豆腐，松鼠鱼，请问您想要吃点什么？")
    MX.media.play()


def get_speak():
    MX.media.record(RS=6)
    return MX.pinyin.getPinyin(MX.speech.STT())


def hello():
    MX.speech.TTS("您好，这是您点的")
    MX.media.play()


while (True):
    time.sleep(3)
    print("going on")
    pos = mc.player.getTilePos()
    mc.postToChat("Your position is x={0} ,y={1} ,z={2}".format(pos.x, pos.y, pos.z))
    if (get_dis() < 1000):
        menu()
        while (True):
            time.sleep(5)
            res = get_speak()
            if (res == 'gongbaojiding。'or res == 'gongbaojidin。'):
                hello()
                GBJD()
                break
            elif (res == 'hongshaorou。'):
                hello()
                HSR()
                break
            elif (res == 'kaishuibaicai'):
                hello()
                KSBC()
                break
            elif (res == 'mapodoufu。'):
                hello()
                MPDF()
                break
            elif (res == 'songshuyu。'):
                hello()
                SSY()
                break
            else:
                mc.postToChat("You said {}".format(res))
                print(res)
                MX.speech.TTS("很抱歉没有听清您的需求，能否再说一遍？")
                MX.media.play()
        time.sleep(4)
        cv2.destroyAllWindows()
    else:
        mc.postToChat("You are too far away from cooker at x=423,y=56,z=113,distense is {}".format(get_dis()))