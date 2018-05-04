#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author:piepis
@file:posttest.py
@time:2018-03-2714:23
@desc:post 请求 server 验证
'''

import  cv2
from wsgiref.simple_server import make_server
from PIL import Image
import numpy
from io import StringIO,BytesIO
# 定义函数，参数是函数的两个参数，都是python本身定义的，默认就行了。
def application(environ, start_response):
    # 定义文件请求的类型和当前请求成功的code
    # start_response('200 OK', [('Content-Type', 'multipart/form-data')])
    # environ是当前请求的所有数据，包括Header和URL，body
    # start_response('200 OK', [('Content-Type', 'multipart/form-data')])
    start_response('200 OK', [('Content-Type', 'application/octet-stream')])
    request_body = environ["wsgi.input"].read(int(environ.get("CONTENT_LENGTH", 0)))
    # request_body
    f = BytesIO(request_body)
    image = Image.open(f)
    img = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
    img.save("one.png")
    t1  = request_body

    # img_buffer=Image.(mode="RGBX",size=[1920,1080],data=request_body)
    # img_buffer.save('E:\git_lib\FacePlateRecognition', 'JPG')
    tt =0
    # input your method here
    # for instance:
    # 增删改查

    dic = {'myNameIs': name, 'myNoIs': no}

    return [json.dumps(dic).encode('utf8')]


if __name__ == "__main__":
    port = 8000
    httpd = make_server("", port, application)
    print ("serving http on port {0}...".format(str(port)))
    httpd.serve_forever()

#
# import socket
#
# def handle_request(client):
#     buf = client.recv(1024)
#     print(buf)
#     msg = "HTTP/1.1 200 OK\r\n\r\n"  #HTTP头信息
#     client.send(('%s' % msg).encode())
#     msg = "Hello, World!"
#     client.send(('%s' % msg).encode())
#
# def main():
#     ip_port = ("localhost", 8000)
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.bind(ip_port)
#     sock.listen(5)
#
#     while True:
#         conn, addr = sock.accept()
#         handle_request(conn)
#         conn.close()
#
# if __name__ == "__main__":
#     main()

# from wsgiref.simple_server import make_server
#
#
# def handle_request(env, res):
#     res("200 OK", [("Content-Type", "text/html")])
#     body = "<h1>Hello World!</h1>"
#     return [body.encode("utf-8")]
#
#
# if __name__ == "__main__":
#     httpd = make_server("", 8000, handle_request)
#     print("Serving http on port 80000")
#     httpd.serve_forever()