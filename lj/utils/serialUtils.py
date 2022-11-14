'''
Author: linin00
Date: 2022-11-14 20:11:03
LastEditTime: 2022-11-14 21:32:09
LastEditors: linin00
Description: 
FilePath: /lj/utils/serialUtils.py

'''
import serial

class Serial :
  def __init__(self, com, timeout = 0) :
    self.__serial = serial.Serial(com,timeout = timeout)
  def readlineb(self) -> bytes:
    return self.__serial.readline()
  def readline(self) -> str:
    return self.__serial.readline().decode()
  def write(self, data:str) :
    return self.__serial.write(data.encode())
  def writeb(self, data:bytes) :
    return self.__serial.write(data)

if __name__ == '__main__':
  ser = Serial('/dev/ttys009', timeout=1)
  while True:
    res = ser.readline()
    if res != '':
      print(res)
      break
    print('waitting')