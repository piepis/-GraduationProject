'''
#!/usr/bin/env python
# encoding: utf-8
@author: piepis
@contact: wangkai@keking.cn
@file: PlateRecognition.py
@time: 2018/3/3 23:03
@desc:车牌识别测试
'''

import cv2
import time
from concurrent.futures import ThreadPoolExecutor
from hyperlpr_py3 import  pipline as  pp
def plate(imagepath):
    image = cv2.imread(imagepath)

    # image,res  = pp.SimpleRecognizePlateByE2E(image)
    # image, res = pp.SimpleRecognizePlate(image)
    executor = ThreadPoolExecutor(max_workers=2)
    t0 = time.time()
    future = executor.submit(pp.SimpleRecognizePlateByE2E, image)
    print(future.done())
    future = executor.submit(pp.SimpleRecognizePlate, image)
    print(future.done())
    t1 = time.time()-t0
    print('车牌识别总时间：{}s'.format(t1))
    print('future{0}'.format(future.result()))
def face(imag):
    t0 = time.time()
    face_cascade = cv2.CascadeClassifier(r'./model/haarcascade_frontalface_default.xml')
    # eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    img = cv2.imread(imag)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        # roi_color = img[y:y+h, x:x+w]
    #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #cv2.imshow('img',img)
    cv2.imwrite('11t.jpg',img)
    t1 = time.time() - t0
    print('脸识别总时间：{}s'.format(t1))
if  __name__=='__main__':
    t0 = time.time()
    imagepath = '11.jpg'
    executor = ThreadPoolExecutor(max_workers=2)
    future = executor.submit(plate, imagepath)
    future = executor.submit(face, imagepath)
    print(future.result())
    t1 = time.time() - t0
    print('总时间：{}s'.format(t1))


# faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 探测图片中的人脸
'''
image – 需要检测的 CV_8U 输入矩阵。
objects – 输出vector载体容器用于保存被识别的物体矩阵。
scaleFactor – 指定每张图片的缩小比例的参数。
minNeighbors – 指定每个候选矩阵至少包含的邻近元素个数。
flags – 与旧版级联分类器模型函数cvHaarDetectObjects的flags相同. 此参数不被用于新版模型。
minSize – 最小可能的对象的大小，小于的对象将被忽略。
maxSize – 最大可能的对象的大小，大于的对象将被忽略。
'''

