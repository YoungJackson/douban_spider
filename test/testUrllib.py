#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@Author:SenYang
#@Time:2021/7/19 10:04
#@File:testUrllib.py
#@Software:PyCharm

import urllib.request
#获取一个get请求
# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8')) #对获取到的网页源码进行utf-8解码

#获取post请求
# import urllib.parse
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response=urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))
# try:
#     response=urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.status)
#     print(response.read().decode("utf-8"))
# except Exception as re:
#     print(re)

# response=urllib.request.urlopen("https://www.baidu.com/")
# print(response.getheader("Server"))

#url="https://www.douban.com/"

import urllib
# url="http://httpbin.org/post"
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
# }
# data=bytes(urllib.parse.urlencode({'name':'Eric'}),encoding="utf-8")
# req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response=urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

url="https://www.douban.com/"
#伪装成浏览器
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70"
}
req = urllib.request.Request(url=url, headers=headers)
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))