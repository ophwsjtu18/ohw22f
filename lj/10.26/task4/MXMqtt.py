'''
Author: linin00
Date: 2022-10-26 18:42:59
LastEditTime: 2022-10-26 18:42:59
LastEditors: linin00
Description: 
FilePath: /lj/10.26/task4/MXMqtt.py

'''
'''
Author: linin00
Date: 2022-10-26 18:37:20
LastEditTime: 2022-10-26 18:37:21
LastEditors: linin00
Description: 
FilePath: /lj/10.26/task3/MXMqtt.py

'''
'''
Author: linin00
Date: 2022-10-26 18:29:04
LastEditTime: 2022-10-26 18:29:04
LastEditors: linin00
Description: 
FilePath: /lj/10.26/task2/MXMqtt.py

'''
import paho.mqtt.client as mqtt
import json
import time
class MXMqtt:

    def __init__(self, host, post):
        self.host = host
        self.post = post
        self.mqttClient = mqtt.Client()
        self.message = None
        self.flag = False
        self.__connect()

    def __connect(self):
        self.mqttClient.connect(self.host, self.post, 60)
        self.mqttClient.loop_start()

    def __messageBack(self, client, userdata, msg):
        self.message = msg
        self.flag = True

    def PUB(self, topic, payload, qos=1):
        """发布信息"""
        self.mqttClient.publish(topic, payload, qos)

    def SUB(self, topic, qos=1):
        """订阅频道"""
        self.mqttClient.subscribe(topic, qos)
        self.mqttClient.on_message = self.__messageBack

    def returnMsg(self):
        """获取返回的消息"""
        if self.flag:
            self.flag = False
            return self.message.payload.decode("utf-8"), self.message.topic
        return None


