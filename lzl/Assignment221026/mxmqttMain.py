from MXMqtt import MXMqtt #导入库文件
import time
#==========连接MQTT服务器===============#
mqtt= MXMqtt("mqtt.16302.com",1883)
#=============订阅频道==================#
mqtt.SUB("JIAODA")
time.sleep(1)

#=============向频道发送信息=============#
mqtt.PUB("JIAODA","HELLO,WORLD")
time.sleep(1)
#=============接收频道信息===============#
da=mqtt.returnMsg()
print(da)