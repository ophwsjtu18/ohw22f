from operator import index
import cv2
import math
import numpy as np
import mcpi.minecraft as minecrafto
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
resize_w = 640
resize_h = 480
rect_height = 0
rect_percent_text = 0

# initialize mc
mc = minecrafto.Minecraft.create()
pos = mc.player.getTilePos()

with mp_hands.Hands(min_detection_confidence=0.7,
                        min_tracking_confidence=0.5,
                        max_num_hands=2) as hands:
    while cap.isOpened():
        success, image = cap.read()
        image = cv2.resize(image, (resize_w, resize_h))
        if not success:
            print("Empty frame.")
            continue

        image.flags.writeable = False
        # convert to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        # mediapipe model processing
        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
        if results.multi_hand_landmarks:
            # every hand
            for hand_landmarks in results.multi_hand_landmarks:
                # draw fingers
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

                Landmark = []
                for landmark_id, finger_axis in enumerate(
                        hand_landmarks.landmark):
                    Landmark.append([
                        landmark_id, finger_axis.x, finger_axis.y,
                        finger_axis.z
                    ])
                if Landmark:
                    __tip = Landmark[8]
                    __tip_x = math.ceil(__tip[1] * resize_w)
                    __tip_y = math.ceil(__tip[2] * resize_h)
                    __mcp = Landmark[5]
                    __mcp_x = math.ceil(__mcp[1] * resize_w)
                    __mcp_y = math.ceil(__mcp[2] * resize_h)
                    # print(thumb_finger_tip_x)
                    tip_point = (__tip_x,__tip_y)
                    mcp_point = (__mcp_x,__mcp_y)

                    # draw two points and the line in between
                    image = cv2.circle(image,tip_point,10,(255,0,255),-1)
                    image = cv2.circle(image,mcp_point,10,(255,0,255),-1)
                    image = cv2.line(image,tip_point,mcp_point,(255,0,255),5)

                    print(__tip_x-__mcp_x)
                    print(__tip_y-__mcp_y)

                    mc.player.setTilePos(pos.x+int(  (__tip_x-__mcp_x)/30  ),pos.y+int(  (-__tip_y+__mcp_y)/30  ),pos.z)  
                    pos = mc.player.getTilePos()

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
