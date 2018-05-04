#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:TcpSocket.py
@time:2018-03-1217:44
@desc:创建TCP/IP 套接字
'''
from  socket import *
from time import ctime
ss = socket()
HOST = '' #表示可以使用任何可用的地址
PORT = 21567 #选择一个端口号 >1024 小于1024的端口号预留给了系统
BUFSIZE = 1024 #设置缓冲区的大小1KB 可调节
ADDR = (HOST,PORT) #元组 存放 IP 和端口号

tcpSerSock = socket(AF_INET,SOCK_STREAM) #分配TCP服务器套接字
tcpSerSock.bind(ADDR)     #将套接字绑定到服务器地址（主机名，端口号对）
tcpSerSock.listen(5)      #设置并启动TCP监听器 并传入连接请求的最大值（5只是个估计值，并不一定准确）
while True:
    print('waiting for connenct ...')
    #tcpCliSock 客户端连接套接字 addr 客户端 IP 和端口信息
    tcpCliSock,addr = tcpSerSock.accept() #被动等待客户端发送消息
    print('...connect from :',addr)
    while True :
        data = tcpCliSock.recv(BUFSIZE) #接收 缓冲区中存储的客户端发过来的数据
        if not data :
            break
        tcpCliSock.send(bytes('[%s] %s' %(ctime(),data),'utf-8')) #将结果return 给客户端
    tcpCliSock.close() #关闭客户端
tcpSerSock.close() #关闭服务端 永远不会被执行。如果要在某条件下退出服务器，可以考虑使用close()
