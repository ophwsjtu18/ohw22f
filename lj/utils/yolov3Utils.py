'''
Author: linin00
Date: 2022-11-08 15:50:32
LastEditTime: 2022-11-08 16:04:46
LastEditors: linin00
Description: 
FilePath: /lj/utils/yolov3Utils.py

'''
import numpy as np
import cv2
import os
import time

class YoloNet:
  def __init__(self, yolo_dir = './utils/yolov3Dir', CONFIDENCE = 0.5, THRESHOLD = 0.4) :
    self.__weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
    self.__configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
    self.__labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
    self.__CONFIDENCE = CONFIDENCE  # 过滤弱检测的最小概率
    self.__THRESHOLD = THRESHOLD  # 非最大值抑制阈值
    with open(self.__labelsPath, 'rt') as f:
        self.__labels = f.read().rstrip('\n').split('\n')
    # 加载网络、配置权重
    self.__net = cv2.dnn.readNetFromDarknet(self.__configPath, self.__weightsPath)  ## 利用下载的文件
  def process(self, img, draw = True) :
    (H, W) = img.shape[:2]
    blobImg = cv2.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)  ## net需要的输入是blob格式的，用blobFromImage这个函数来转格式
    self.__net.setInput(blobImg)  ## 调用setInput函数将图片送入输入层
    outInfo = self.__net.getUnconnectedOutLayersNames()  ## 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
    layerOutputs = self.__net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
    boxes = [] # 所有边界框（各层结果放一起）
    confidences = [] # 所有置信度
    classIDs = [] # 所有分类ID
    for out in layerOutputs:  # 各个输出层
        for detection in out:  # 各个框框
            # 拿到置信度
            scores = detection[5:]  # 各个类别的置信度
            classID = np.argmax(scores)  # 最高置信度的id即为分类id
            confidence = scores[classID]  # 拿到置信度
            # 根据置信度筛查
            if confidence > self.__CONFIDENCE:
                box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
    #应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.__CONFIDENCE, self.__THRESHOLD) # boxes中，保留的box的索引index存入idxs
    # 应用检测结果
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(self.__labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
    if draw and len(idxs) > 0:
        for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
            text = "{}: {:.4f}".format(self.__labels[classIDs[i]], confidences[i])
            cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
