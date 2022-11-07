from operator import index
import cv2
import mediapipe as mp
import time
import math
import numpy as np
import mcpi.minecraft as MC 

#initialize mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# initialize OpenCV (video flow and set sizes)
cap = cv2.VideoCapture(0)
resize_w = 640
resize_h = 480
rect_height = 0
rect_percent_text = 0

# initialize mc
mc = MC.Minecraft.create()
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

                # fingers[]: (x,y)
                landmark_list = []
                for landmark_id, finger_axis in enumerate(
                        hand_landmarks.landmark):
                    landmark_list.append([
                        landmark_id, finger_axis.x, finger_axis.y,
                        finger_axis.z
                    ])
                if landmark_list:
                    # index finger tip
                    index_finger_tip = landmark_list[8]
                    index_finger_tip_x = math.ceil(index_finger_tip[1] * resize_w)
                    index_finger_tip_y = math.ceil(index_finger_tip[2] * resize_h)
                    # index finger mcp
                    index_finger_mcp = landmark_list[5]
                    index_finger_mcp_x = math.ceil(index_finger_mcp[1] * resize_w)
                    index_finger_mcp_y = math.ceil(index_finger_mcp[2] * resize_h)
                    # print(thumb_finger_tip_x)
                    tip_point = (index_finger_tip_x,index_finger_tip_y)
                    mcp_point = (index_finger_mcp_x,index_finger_mcp_y)

                    # draw two points and the line in between
                    image = cv2.circle(image,tip_point,10,(255,0,255),-1)
                    image = cv2.circle(image,mcp_point,10,(255,0,255),-1)
                    image = cv2.line(image,tip_point,mcp_point,(255,0,255),5)

                    print(index_finger_tip_x-index_finger_mcp_x)
                    print(index_finger_tip_y-index_finger_mcp_y)

                    # send v to mc
                    mc.player.setTilePos(pos.x+int(  (index_finger_tip_x-index_finger_mcp_x)/30  ),pos.y+int(  (-index_finger_tip_y+index_finger_mcp_y)/30  ),pos.z)  
                    pos = mc.player.getTilePos()
        # show image
        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()