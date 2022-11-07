import cv2
import mediapipe as mp
from math import sqrt
import mcpi.minecraft as minecraft
import pyautogui as ui

ui.FAILSAFE = False
ui.PAUSE = 0.01
LEFT = 1
RIGHT = 2
FORWARD = 3
BACKWARD = 4
STANDBY = 5

# mc = minecraft.Minecraft.create()
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

x = [0 for i in range(21)]
y = [0 for i in range(21)]


def getDis(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def getDrection(x1, y1, x2, y2):
    if abs(x1 - x2) < 30:
        if y1 < y2 and getDis(x1, y1, x2, y2) >= 80:
            # print("forward",getDis(x1, y1, x2, y2))
            return FORWARD
        elif y1 > y2 and getDis(x1, y1, x2, y2) >= 80:
            # print("backward",getDis(x1, y1, x2, y2))
            return BACKWARD
    elif abs(y1 - y2) < 60:
        if x1 < x2 and getDis(x1, y1, x2, y2) >= 40:
            # print("left",getDis(x1, y1, x2, y2))
            return LEFT
        elif x1 > x2 and getDis(x1, y1, x2, y2) >= 40:
            # print("right",getDis(x1, y1, x2, y2))
            return RIGHT
    return STANDBY


def findHands(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.putText(img, str(int(id)), (cx + 10, cy + 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


def hands2direction(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    dir = STANDBY
    flag = False
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                for i in [0, 2, 4, 5, 8, 12, 16, 20]:
                    if id == i:
                        x[i], y[i] = cx, cy
                        # print(i,":",x[i],y[i])

                for a in [4, 12, 16, 20]:
                    for b in [4, 12, 16, 20]:
                        if getDis(x[a], y[a], x[b], y[b]) > 80:
                            flag = False
                            break
                        else:
                            flag = True
                if flag:
                    dir = getDrection(x[8], y[8], x[5], y[5])

                for a in [8, 12, 16, 20]:
                    for b in [8, 12, 16, 20]:
                        if getDis(x[a], y[a], x[b], y[b]) > 80:
                            flag = False
                            break
                        else:
                            flag = True
                if (flag):
                    dir = getDrection(x[4], y[4], x[2], y[2])

    return dir


def display(dir):
    if dir == FORWARD:
        cv2.putText(img, "forword", (x[8] - 20, y[8] - 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
    if dir == BACKWARD:
        cv2.putText(img, "backward", (x[8] - 20, y[8] + 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
    if dir == RIGHT:
        cv2.putText(img, "right", (x[4] + 40, y[4]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)
    if dir == LEFT:
        cv2.putText(img, "left", (x[4] - 40, y[4]), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2)


def direction2move(dir):
    if dir == FORWARD:
        ui.keyDown('W')
        ui.keyUp('A')
        ui.keyUp('S')
        ui.keyUp('D')
    elif dir == BACKWARD:
        ui.keyDown('S')
        ui.keyUp('W')
        ui.keyUp('A')
        ui.keyUp('D')
    elif dir == LEFT:
        ui.keyDown('A')
        ui.keyUp('W')
        ui.keyUp('S')
        ui.keyUp('D')
    elif dir == RIGHT:
        ui.keyDown('D')
        ui.keyUp('W')
        ui.keyUp('A')
        ui.keyUp('S')
    else:
        ui.keyUp('W')
        ui.keyUp('A')
        ui.keyUp('S')
        ui.keyUp('D')
    return


cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    img = cv2.flip(frame, 1)
    findHands(img)
    dir = hands2direction(img)
    display(dir)
    direction2move(dir)
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
