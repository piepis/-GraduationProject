#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:PedestrainExtract.py
@time:2018-04-1716:41
@desc:单个行人提取
'''

import re
import os
import cv2
#读取txt文本
def gettext(filePath):
    row_list = []
    with open(filePath,'r') as file_to_read:
        lines = file_to_read.read() # 整行读取数据
        Imagefilename = re.search(r'Image filename :.*\"(.*\.png)\"', lines) #图片存放路径
        PASperson_re = re.findall(r'Bounding box for object \d "PASperson" \(Xmin, Ymin\) - \(Xmax, Ymax\) :.*(\(\d*, \d*\) - \(\d*, \d*\))', lines) #图片的坐标
        row_list.append(Imagefilename.group(0).split("\"")[1])
        for str in PASperson_re:
            PASperson = re.findall('(\d{1,3}).',str)
            row_list.append(PASperson)
    return row_list
#分割图片
def splitImg(dir,list):
    Imagefilename = list[0]
    ImgfilePath = os.path.join(dir, Imagefilename)
    Img = cv2.imread(ImgfilePath)
    cropImgname = re.split(r"/",Imagefilename)[2] #分割的图片名字
    str1,str2=cropImgname.split('.')
    i =1
    for coordinate in list[1:] :
        Xmin,Ymin,Xmax,Ymax = coordinate
        cropImg = Img[int(Ymin):int(Ymax),int(Xmin):int(Xmax)]
        #cropImg = cv2.resize(cropImg,(594, 720))
        cv2.imwrite(os.path.join(os.path.join(dir,'splitImg'), '{0}_{1}.{2}'.format(str1,i,str2)),cropImg)
        i=i+1

def main(dir):
    txtdir = os.path.join(dir,r'Test\annotations')
    for file  in  os.listdir(txtdir):
        splitImg(dir, list=gettext(filePath=os.path.join(txtdir,file)))

if __name__ == '__main__':
    dir =r'H:\opencv\INRIAPerson'
    main(dir)
