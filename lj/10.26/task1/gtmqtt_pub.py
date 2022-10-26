'''
Author: linin00
Date: 2022-10-26 18:11:06
LastEditTime: 2022-10-26 18:12:52
LastEditors: linin00
Description: 
FilePath: /lj/10.26/task1/gtmqtt_pub.py

'''
import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

def main() :
  client = mqtt_client.Client(client_id)
  client.on_connect = on_connect
  client.connect(broker, port)
  client.loop_start()

  msg_count=0

  while True:
      msg_count+=1
      time.sleep(1)
      msg = f"messages: {msg_count}"
      result = client.publish(topic, msg)
      print(result)

if __name__ == "__main__":
  main()