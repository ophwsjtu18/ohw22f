'''
Author: linin00
Date: 2022-11-02 12:00:55
LastEditTime: 2022-11-08 22:36:01
LastEditors: linin00
Description: 
FilePath: /lj/utils/Hand.py

'''

import cv2
import mediapipe as mp
import time
from cv2Face2Dir import Direction
import numpy as np

class HandDetector():
  def __init__(self,
              mode=False,
              maxHands=1,
              minDetectionConfidence=0.5,
              minTrackingConfidence=0.5):
    self.__mpHands = mp.solutions.hands
    self.__hands = self.__mpHands.Hands(
      static_image_mode=mode,
      max_num_hands=maxHands,
      min_detection_confidence=minDetectionConfidence,
      min_tracking_confidence=minTrackingConfidence
    )
    self.__mpDraw = mp.solutions.drawing_utils

  def findHands(self, img, draw = True):
    imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    self.__results = self.__hands.process(imRGB)
    if draw and self.__results.multi_hand_landmarks :
      for handsLms in self.__results.multi_hand_landmarks :
        self.__mpDraw.draw_landmarks(img, handsLms, self.__mpHands.HAND_CONNECTIONS)

  def trackLandmark(self, img, index, draw = True):
    res = []
    if self.__results.multi_hand_landmarks :
      for handsLms in self.__results.multi_hand_landmarks :
        for id, lm in enumerate(handsLms.landmark) :
          h, w, c = img.shape
          cx, cy = int (lm.x * w), int(lm.y * h)
          if (id == index) :
            if draw :
              cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
            res.append([cx, cy])
    return res

  def trackLandmarks(self, img, draw = True):
    res = []
    if self.__results.multi_hand_landmarks :
      for handsLms in self.__results.multi_hand_landmarks :
        for id, lm in enumerate(handsLms.landmark) :
          h, w, c = img.shape
          cx, cy = int (lm.x * w), int(lm.y * h)
          res.append([cx, cy])
          if draw :
            cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
    return res
  def _getLandmarks(self):
    return self.__results.multi_hand_landmarks


class Hand2Direction():
  def __init__(self):
    self.__hand = HandDetector()
  def __help(self, shape, pos):
    w, h = shape
    x, y = pos
    p1 = (w/3, h/3)
    p2 = (2 * w/3, h/3)
    p3 = (w/3, 2 * h/3)
    p4 = (2 * w/3, 2 * h/3)
    if x > p1[0] and x < p2[0] and y < p3[1] and y > p1[1]:
      return Direction.STANDBY
    if x < p1[0] :
      if y > p3[1] and y < p1[1]:
        return Direction.LEFT
      if y > p1[1] and x/y < w/h :
          return Direction.LEFT
      if y < p3[1] and x/(h - y) < w/h :
          return Direction.LEFT
    if x > p2[0]:
      if y > p3[1] and y < p1[1]:
        return DIRECTION.RIGHT
      if y > p1[1] and (w - x)/h < w/h :
          return Direction.RIGHT
      if y < p3[1] and (w - x)/(h - y) < w/h :
          return Direction.RIGHT
    if y > p3[1] :
      return Direction.BACKWARD
    if y < p1[1] :
      return Direction.FORWARD

  def direction(self, img, index, draw = True):
    h, w = img.shape[0], img.shape[1]
    self.__hand.findHands(img, draw)
    pos = self.__hand.trackLandmark(img, index, draw)
    print(h, w)
    print(pos)
    if len(pos) != 1 :
      return Direction.NOFACE
    rx, ry = pos[0][1], pos[0][2]
    return self.__help((w, h), (rx, ry))

def finger_stretch_detect(point1, point2, point3):
  result = 0
  dist1 = np.linalg.norm((point2 - point1), ord=2)
  dist2 = np.linalg.norm((point3 - point1), ord=2)
  if dist2 > dist1:
      result = 1
  return result

def detect_hands_gesture(result):
    if (result[0] == 1) and (result[1] == 0) and (result[2] == 0) and (result[3] == 0) and (result[4] == 0):
        gesture = "good"
    elif (result[0] == 0) and (result[1] == 1)and (result[2] == 0) and (result[3] == 0) and (result[4] == 0):
        gesture = "one"
    elif (result[0] == 0) and (result[1] == 0)and (result[2] == 1) and (result[3] == 0) and (result[4] == 0):
        gesture = "please civilization in testing"
    elif (result[0] == 0) and (result[1] == 1)and (result[2] == 1) and (result[3] == 0) and (result[4] == 0):
        gesture = "two"
    elif (result[0] == 0) and (result[1] == 1)and (result[2] == 1) and (result[3] == 1) and (result[4] == 0):
        gesture = "three"
    elif (result[0] == 0) and (result[1] == 1)and (result[2] == 1) and (result[3] == 1) and (result[4] == 1):
        gesture = "four"
    elif (result[0] == 1) and (result[1] == 1)and (result[2] == 1) and (result[3] == 1) and (result[4] == 1):
        gesture = "five"
    elif (result[0] == 1) and (result[1] == 0)and (result[2] == 0) and (result[3] == 0) and (result[4] == 1):
        gesture = "six"
    elif (result[0] == 0) and (result[1] == 0)and (result[2] == 1) and (result[3] == 1) and (result[4] == 1):
        gesture = "OK"
    elif(result[0] == 0) and (result[1] == 0) and (result[2] == 0) and (result[3] == 0) and (result[4] == 0):
        gesture = "stone"
    else:
        gesture = "not in detect range..."
    
    return gesture
class Gesture2Direction(HandDetector):
  def __init__(self,
              mode=False,
              maxHands=1,
              minDetectionConfidence=0.5,
              minTrackingConfidence=0.5):
    super(Gesture2Direction, self).__init__(
      mode,
      maxHands,
      minDetectionConfidence,
      minTrackingConfidence
    )
  def __help(self, landmark):
    if len(landmark) :
        figure = np.zeros(5)
        for k in range(0, 5):
          if k == 0:
              figure_ = finger_stretch_detect(landmark[17],landmark[4*k+2],landmark[4*k+4])
          else:    
              figure_ = finger_stretch_detect(landmark[0],landmark[4*k+2],landmark[4*k+4])
          figure[k] = figure_
        gesture_result = detect_hands_gesture(figure)
        # print(f"{gesture_result}")
        if gesture_result == "one" :
          return Direction.FORWARD
        if gesture_result == "two" :
          return Direction.BACKWARD
        if gesture_result == "five" :
          return Direction.LEFT
        if gesture_result == "good" :
          return Direction.RIGHT
        return Direction.STANDBY
    else :
      return Direction.NOFACE
  def direction(self, img):
    self.findHands(img)
    lms = self.trackLandmarks(img, False)
    if len(lms) == 0 :
      return Direction.NOFACE
    landmark = np.empty((21, 2))
    for j, lm in enumerate(lms):
      landmark_ = [lm[0], lm[1]]
      landmark[j,:] = landmark_
    return self.__help(landmark)

if __name__ == '__main__':
  cap = cv2.VideoCapture(0)
  cTime = 0
  pTime = 0
  hands = HandDetector()
  while True :
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands.findHands(img)
    res = hands.trackLandmark(img, 8)
    print(res)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), 
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)  
    if cv2.waitKey(1) & 0xff == ord('q'):
      break