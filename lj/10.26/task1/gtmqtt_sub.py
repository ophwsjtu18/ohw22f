'''
Author: linin00
Date: 2022-10-26 18:09:55
LastEditTime: 2022-10-26 18:21:57
LastEditors: linin00
Description: 
FilePath: /lj/10.26/task1/gtmqtt_sub.py

'''
import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "sjtu2022f"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


def on_message(client, userdata, msg):
    print(f"Received {msg.payload.decode()} from {msg.topic} topic")

def main() :
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()

if __name__ == '__main__':
    main()