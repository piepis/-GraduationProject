#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:FtpServer.py
@time:2018-03-1515:53
@desc:文件服务器
'''
import socketserver
import os
# Format: name_len      --- one byte
#         name          --- name_len bytes
#         data          --- variable length
# Save data to name into current directory
addr = ('127.0.0.1', 1234)
class MyTCPHandler (socketserver.StreamRequestHandler):
        def handle (self):
                name_len = ord(self.rfile.read(1))
                name = self.rfile.read(name_len)
                print ("Get request:%s"%name)
                dir = bytes('E:\git_lib\新建文件夹','utf-8')
                tt =os.path.join(dir,name)
                fd = open(tt, 'wb')
                cont = self.rfile.read(4096)
                while cont:
                        fd.write(cont)
                        cont = self.rfile.read(4096)
                fd.close()
                self.request.sendall(bytes(self.client_address,'utf'))
                print ("Out :%s"%name)

server = socketserver.TCPServer(addr, MyTCPHandler)
server.serve_forever()

