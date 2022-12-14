import numpy as np 
import cv2
import random
import time
from paho.mqtt import client as mqtt_client

# mqtt initialize
broker = 'broker.emqx.io'
port = 1883
topic = "sjtu2022s-mccontrol02"
client_id = 'python-mqtt-{random.randint(0, 1000)}'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

msg_count=0

#face cascade initialize
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# capture image
while (1):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    img = cv2.flip(frame,1)
    cv2.imshow('frame',img)
    
    # face cascade
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    height = img.shape[0]
    width = img.shape[1]

    # publish commands
    for (x,y,w,h) in faces:
        if x<width/3:
            msg = "left"
            time.sleep(1)
            result = client.publish(topic, msg)
            print(result)
        if x>width/2:
            msg = "right"
            time.sleep(1)
            result = client.publish(topic, msg)
            print(result)
        if y<height/3:
            msg = "up"
            time.sleep(1)
            result = client.publish(topic, msg)
            print(result)
        if y>height/2:
            msg = "down"
            time.sleep(1)
            result = client.publish(topic, msg)
            print(result)
        if w<width/3:
            msg = "back"
            time.sleep(1)
            result = client.publish(topic, msg)
            print(result)
        if w>width/2:
            msg = "forward"
            time.sleep(1)
            result = client.publish(topic, msg)
            print(result)
   
    if cv2.waitKey(1) & 0xFF == 27:
            break

cv2.waitKey(0)
cv2.destroyAllWindows()
