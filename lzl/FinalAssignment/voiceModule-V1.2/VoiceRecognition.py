from moocxing.package import MOOCXING
from aip import AipSpeech
import subprocess
import os
import pyaudio
from mcpi.minecraft import Minecraft
APP_ID = '25496064'
API_KEY = "A6fXM6nA1B8GY2txDIUCXYyu"
SECRET_KEY = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8"
mc = Minecraft.create()
# MOOCXING 库
# https://gitee.com/Azanzhi/moocxing#1-%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE
# 要用默认名字MX
# 需要Visual C++ Build Tools
MX = MOOCXING.INIT() # 最大录音时间


# 直接将文本打印到MC聊天栏
# name是说话人的名字，text是话语
# 一些台词如下：
# 室友 这比后室还离谱……
def textToChat(name, text):
    mc.postToChat(name+": "+text)
    return

# 陌生人直接说话,调用百度库改变声音
def textToVoiceStranger():
    stanger_text = "在这个世界的每一千年，校园中会出现天球交汇之地，其中有三颗宝石，集齐之后即可实现任何愿望。但是，从未有人走出来过。"
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    voice = client.synthesis(stanger_text, 'zh', 6, {'vol': 15, 'per': 3, 'spd': 5})
    with open("stranger_voice.mp3", 'wb') as fp:
        fp.write(voice)
    if not os.path.exists("stranger_voice.wav"):
        subprocess.call(['ffmpeg', '-i', 'stranger_voice.mp3', 'stranger_voice.wav'])
    fp.close()
    MX.media.play("stranger_voice.wav")
    textToChat("陌生人", "在这个世界的每一千年，校园中会出现天球交汇之地，其中有三颗宝石，集齐之后即可实现任何愿望.")
    textToChat("陌生人", "但是，从未有人走出来过.")
    return

# 小帅和室友的功能，录音，转化成文字发到chat框里面
# 最多说7秒钟，可以在上面的RS里调
def voiceToChat(name):
    # MX.media.record(max_time, "shuaivoice_temp.wav")
    # record_text = MX.speech.STT("shuaivoice_temp.wav", _print=True)
    MX.media.record(RS=7)
    record_text = MX.speech.STT(_print=True)
    textToChat(name, record_text)
    return name+": "+record_text

# 小美的功能,从聊天框里面获取小帅的话，并且给出相应的回答
# 用法1:chatToVoice("")录音，从小帅的话里面找出关键词回答
# 用法2：chatToVoice(text) 是用来打表的,直接让小美说话，不录音
# 比如 小美 我相信你，也许我能帮你离开这里。
# 小美 看,接下来就交给你研究了.
# 小美 我可以成为信息中转的桥梁.
# 小美 我的任务就要结束了.每次帮助迷路的人离开这里时,我的记忆就会被重置。
# 小美 但是,我仍然想看看他们来的那个世界是什么样子的,能帮我这个忙吗?

# 默认女声

def chatToVoice(mei_text=""):


    if mei_text != "":
        MX.speech.TTS(mei_text)
        MX.media.play()
        textToChat("小美", mei_text)
        return
    chatEventMsg = ""
    chatEventMsg =  voiceToChat("小帅")

    if "小帅" in chatEventMsg:
        shuai_text = chatEventMsg.lstrip("小帅: ")# 保留小帅纯话语
        if "你是谁" in shuai_text:
            mei_text = "我只是一个机器人，作为引导者，寻找那些还抱有希望的人们，回到原本的世界。"
            MX.speech.TTS(mei_text)
            MX.media.play()
        if "你能帮我吗" in shuai_text:
            mei_text = "跟我来吧，我带你去！"
            MX.speech.TTS(mei_text)
            MX.media.play()
        if "扫描地图" in shuai_text:
            mei_text = "这对于我来说还是挺容易的。"
            MX.speech.TTS(mei_text)
            MX.media.play()
        if "我一定会的" in shuai_text:
            mei_text = "谢谢你,再见了。"
            MX.speech.TTS(mei_text)
            MX.media.play()
        if mei_text != "":
            textToChat("小美", mei_text)
            return

    return
