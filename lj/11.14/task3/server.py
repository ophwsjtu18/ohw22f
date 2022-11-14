'''
Author: linin00
Date: 2022-11-14 21:18:47
LastEditTime: 2022-11-14 21:47:20
LastEditors: linin00
Description: 
FilePath: /lj/11.14/task3/server.py

'''
import sys
sys.path.append('./utils')
from cv2Utils import waitKey
import cv2
from lightUtils import Light
from cv2Face2Dir import Direction
from serialUtils import Serial

serial = Serial('/dev/ttys009', timeout=1)
def getDirection() -> Direction :
  command = serial.readline()
  res = Direction.STANDBY
  print(command)
  if command == "forward\n":
    res = Direction.FORWARD
  elif command == "backward\n":
    res = Direction.BACKWARD
  elif command == "left\n":
    res = Direction.LEFT
  elif command == "right\n":
    res = Direction.RIGHT
  elif command == "~":
    quit()
  return res

if __name__ == '__main__':
  light = Light()
  print('init')
  while True:
    dir = getDirection()
    light.direction(dir)
    light.show()
    if waitKey(1, 'q'):
      break

