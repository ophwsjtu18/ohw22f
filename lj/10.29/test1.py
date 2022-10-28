'''
Author: linin00
Date: 2022-10-29 03:55:05
LastEditTime: 2022-10-29 04:25:51
LastEditors: linin00
Description: 
FilePath: /10.29/test1.py

'''
import numpy as np

def dot(a, b) -> np.array:
  return np.dot(a, b)

def Test1() :
  a = np.array([1, 2, 3, 4, 5]) # 一维空间中的5个点坐标
  b = np.array([[1],[2],[3],[4],[5]])
  c = np.array([[1, 2, 3, 4, 5]]) # 五维空间中的一个点坐标
  # print 函数打印的是这个矩阵在内存的样子
  print(a, a.T)
  print(b, b.T) # b 的转置不是[1,2,3,4,5]而是[[1,2,3,4,5]]
  print(c, c.T)
def Test2() :
  a = np.array([1, 2, 3, 4, 5]) # 一维空间中的5个点坐标
  b = np.array([[1],[2],[3],[4],[5]])
  c = np.array([[1, 2, 3, 4, 5]]) # 五维空间中的一个点坐标
  print(dot(a, b))
  # print(dot(a, b.T)) # 报错
  # 原因是b 在内存中是一列
  # 同理 c在内存中是一行，所以下面这一句可以正常执行
  print(dot(a, c.T))
def Test3() :
  a = [1,2,3,2,4,3,5,3]
  print(a)
  print(sorted(a))

if __name__ == '__main__':
  Test3()