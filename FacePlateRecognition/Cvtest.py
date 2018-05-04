#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:Cvtest.py
@time:2018-03-0115:37
@desc: cv2 测试
'''

import cv2

# cv2.imread(文件名，属性) 读入图像
img = cv2.imread('111.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.namedWindow(窗口名，属性) 创建一个窗口
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.imshow(窗口名，图像文件) 显示图像
cv2.imshow('image',img)
print(img.size)