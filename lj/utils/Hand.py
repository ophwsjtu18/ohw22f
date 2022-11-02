'''
Author: linin00
Date: 2022-11-02 12:00:55
LastEditTime: 2022-11-02 18:05:01
LastEditors: linin00
Description: 
FilePath: /lj/utils/Hand.py

'''

import cv2
import mediapipe as mp
import time
from cv2Face2Dir import Direction

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
            res.append([id, cx, cy])
    return res

  def trackLandmarks(self, img, draw = True):
    res = []
    if self.results.multi_hand_landmarks :
      for handsLms in self.results.multi_hand_landmarks :
        for id, lm in enumerate(handsLms.landmark) :
          h, w, c = img.shape
          cx, cy = int (lm.x * w), int(lm.y * h)
          res.append([id, cx, cy])
          if draw :
            cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
    return res


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