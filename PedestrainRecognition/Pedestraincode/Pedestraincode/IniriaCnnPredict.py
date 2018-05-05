#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:IniriaCnnPredict.py
@time:2018-04-2511:58
@desc:行人预测
'''
import cv2
import pandas as pd

import numpy as np
from imutils.object_detection import non_max_suppression
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
#加载预测模型
model = load_model('./model/INIRIA.h5')
def preTest():
    test_datagen = ImageDataGenerator(rescale=1./255)
    test_generator = test_datagen.flow_from_directory(
        'test1',
        target_size = (100,290),
        batch_size =1,
        shuffle=False,
        class_mode ='binary'
    )
    preresult = model.predict_generator(test_generator, 1)
    print(model.predict_generator(test_generator,1))
    if preresult[0][0]>0.9:
        return True
    else:
        return False
#
print ("__file__=%s" % __file__)

# 
image = cv2.imread('crop001038.png')
# print('test after load: ', model.predict(image))
# 初始化我们的行人检测器
#初始化方向梯度直方图描述子
hog = cv2.HOGDescriptor()
#设置支持向量机(Support Vector Machine)使得它成为一个预先训练好了的行人检测器
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)
#使用非极大抑制 避免边框重叠
rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)
t=1
#画出图形
for (xA, yA, xB, yB) in pick:
    cropImg = image[xA:xB, yA:yB]
    # cv2.imwrite( 'test1/test/cropImg{0}.png'.format(t),cropImg)
    # result = preTest()
    # if result:
    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
#图形展示
cv2.imshow("After NMS", image)
cv2.waitKey(0)
