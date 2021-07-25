#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@Author:SenYang
#@Time:2021/7/19 17:41
#@File:testBS4.py
#@Software:PyCharm

from bs4 import BeautifulSoup

file=open("./baidu.html","rb")
html=file.read().decode("utf-8")
bs=BeautifulSoup(html,"html.parser")


#文档遍历
#print(bs.head.contents[1])

#文档搜索
#(1)查找所有 findAll() find_all()
#字符串过滤：查找与字符串完全匹配的内容
# t_list=bs.findAll("a")
# t_list2=bs.find_all("a")
#print(t_list==t_list2)

#(2)正则查找：search()查找
# import re
# t_list=bs.find_all(re.compile("a"))
# print(t_list)

#(3)方法搜索，传入函数根据函数要求搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exists)
#
# for item in t_list:
#   print(item)
# #print(t_list)

#2.kwargs,参数
#t_list=bs.find_all(id="head")
# t_list=bs.find_all(alt="到百度首页")
# for item in t_list:
#   print(item)

#3.Text参数\
import re
#t_list=bs.find_all(text = re.compile("\d"))
# t_list=bs.find_all(text =  "吴亦凡")
# for item in t_list:
#   print(item)
#4.Limit参数
# t_list=bs.find_all("a",limit=3)
# for item in t_list:
#   print(item)

#css选择器
#t_list=bs.select(".manv")#通过类名查找
#t_list=bs.select("#u1") 通过Id查找
#t_list=bs.select("a[class='bri']")#通过属性查找

#t_list=bs.select("head>title")#通过子标签查找

# t_list=bs.select(".mnav ~ .bri")
# print(t_list[0].get_text())
# for item in t_list:
#   print(item)

###-----------------------------------------
#print(type(bs.a))
#print(type(bs.head))
#print("end")
#1,Tag 标签及其内容：拿到找到的第一个内容

#print(type(bs.title.string))
#print(bs.a.attrs)
#2,NavigableString 标签内容

# print(bs)
#3,BeautifulSoup 整个文档

#4,Comment 特殊的NavigableString，输出不包含符号
#
# print(bs.a.string)
# print(type(bs.a.string))


#---------------------------

