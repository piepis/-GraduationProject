#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:PedestrainRec.py
@time:2018-04-1618:30
@desc:行人检测
'''
# 引入所需要的库
from __future__ import print_function  #确保代码同时在Python2.7和Python3上兼容
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils   #安装库pip install imutils ；pip install --upgrade imutils更新版本大于v0.3.1
import cv2

# 初始化我们的行人检测器
#初始化方向梯度直方图描述子
hog = cv2.HOGDescriptor()
#设置支持向量机(Support Vector Machine)使得它成为一个预先训练好了的行人检测器
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

'''
构造了一个尺度scale=1.05的图像金字塔，以及一个分别在x方向和y方向步长为(4,4)像素大小的滑窗
scale的尺度设置得越大，在图像金字塔中层的数目就越少，相应的检测速度就越快，但是尺度太大会导致行人出现漏检；
同样的，如果scale设置得太小，将会急剧的增加图像金字塔的层数，这样不仅耗费计算资源，而且还会急剧地增加检测过程
中出现的假阳数目(也就是不是行人的被检测成行人)。这表明，scale是在行人检测过程中它是一个重要的参数，
需要对scale进行调参。我会在后面的文章中对detectMultiScale中的每个参数做些调研。
'''

# detect people in the image：
(rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
    padding=(8, 8), scale=1.05)