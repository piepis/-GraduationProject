#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:ThreadTcpClient.py
@time:2018-03-1417:34
@desc:多线程实现 TCP 客户端
'''
import socket
def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print ("Received: {}".format(response))
    finally:
        sock.close()

if __name__ == "__main__":
    HOST, PORT = "localhost", 21567
    ip, port =  HOST, PORT
    client(ip, port, "Hello World 1")
    # client(ip, port, "Hello World 2")
    # client(ip, port, "Hello World 3")


