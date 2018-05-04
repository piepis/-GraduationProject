#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:FtpClient.py
@time:2018-03-1515:54
@desc: Ttp客户端
'''
from socket import *
import os.path
target = ('127.0.0.1',1234)
def get_header (name):
        leng = len(name)
        assert leng < 250
        return chr(leng) + name

def send_file (name):
        # basename = os.path.basename(name)
        # header = bytes(get_header(basename),'utf-8')
        cont = open(name,'rb').read()
        s = socket (AF_INET, SOCK_STREAM)
        s.connect(target)
        # s.sendall (header)
        s.sendall (cont)
        s.close()

send_file ('E:\git_lib\img2.jpg')

