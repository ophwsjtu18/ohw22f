import numpy as np 
import cv2
import random
import time
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
topic = "sjtu2022_mc"
client_id = 'python-mqtt-{random.randint(0, 1000)}'

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected Successfully!")
    else:
        print("Failed to connect %d\n", rc)

def print_face(msg):
    time.sleep(1)
    result = client.publish(topic, msg)
    print(result)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

msg_count=0

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while (1):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    img = cv2.flip(frame,1)
    cv2.imshow('frame',img)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    height = img.shape[0]
    width = img.shape[1]

    for (x,y,w,h) in faces:
        if x<width/3:
            msg = "left"
            print_face(msg)
        if x>width/2:
            msg = "right"
            print_face(msg)
        if y<height/3:
            msg = "up"
            print_face(msg)
        if y>height/2:
            msg = "down"
            print_face(msg)
        if w<width/3:
            msg = "back"
            print_face(msg)
        if w>width/2:
            msg = "forward"
            print_face(msg)
   
    if 0xFF == 27 & cv2.waitKey(1):
            break

cv2.waitKey(0)
cv2.destroyAllWindows()
