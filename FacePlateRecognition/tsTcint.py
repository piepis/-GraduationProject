#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:tsTcint.py
@time:2018-03-1219:04
@desc:TcpSockt 的客户端
'''
import time
from socket import *
HOST = "39.107.81.37"
PORT = 8080
BUFSIZE =1024*1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM) #创建套接字
tcpCliSock.connect(ADDR)    #连接套接字
# with open("11.jpg", 'rb') as fil:
dir= bytes('11.jpg')
cont=dir
# cont = open(dir,'rb').read()
# image=dir
# imagepath = bytes(image,'utf-8')
# x = img.tobytes()
# img = cv2.imdecode(np.fromstring(x, np.uint8))

tcpCliSock.sendall(cont)  #发送输入内容
data1 = tcpCliSock.recv(BUFSIZE) #接收服务端处理结果
str1 = str(data1, "utf-8")
print(str1)
# cv2.imwrite('ttttt.jpg',data)
# tcpCliSock.close()



