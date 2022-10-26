'''
Author: linin00
Date: 2022-10-26 18:37:25
LastEditTime: 2022-10-26 18:40:19
LastEditors: linin00
Description: 
FilePath: /lj/10.26/task3/demo.py

'''
from MXMqtt import MXMqtt
import time

if __name__ == '__main__':
  mqtt = MXMqtt("mqtt.16302.com", 1883)
  mqtt.PUB("LJ", "STAND BY")
  time.sleep(1)
