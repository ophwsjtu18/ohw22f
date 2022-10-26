'''
Author: linin00
Date: 2022-10-26 18:29:35
LastEditTime: 2022-10-26 18:32:38
LastEditors: linin00
Description: 
FilePath: /lj/10.26/task2/demo.py

'''
from MXMqtt import MXMqtt
import time

if __name__ == '__main__':
  mqtt = MXMqtt("mqtt.16302.com", 1883)
  mqtt.SUB("lianjie")
  time.sleep(1)
  mqtt.PUB("lianjie", "大江东去浪淘尽")
  time.sleep(1)
  da = mqtt.returnMsg()
  print(da)