#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:ThreadTcp.py
@time:2018-03-1417:32
@desc:多线程实现 TCP
'''
import numpy as np
import cv2
import socketserver
class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('New connection:', self.client_address)
        while True:
            data = self.request.recv(1024*1024)
            image = np.asarray(bytearray(data), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
            # x = np.fromfile(data, dtype=np.ubyte)
            cv2.imwrite('tttttttt1111.jpg',image)
            str = '字符串检验'
            response = bytes(str, 'utf-8')
            self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):#继承ThreadingMixIn表示使用多线程处理request，注意这两个类的继承顺序不能变
    pass

if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 21567
    server = socketserver.ThreadingTCPServer(('127.0.0.1',21567),ThreadedTCPRequestHandler)    #$ 实现多线程的socket
    server.serve_forever()    #$ 当前连接断开不会出现关闭或报错，可以与其他客户端继续连接
