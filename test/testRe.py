#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@Author:SenYang
#@Time:2021/7/20 9:15
#@File:testRe.py
#@Software:PyCharm

#正则表达式

import re

# #创建模式对象
# pat=re.compile("AA")#
# print(pat.findall("AABCAASKDJ"))

# m=re.search("asd","Aasd")
# print(m)

#print(re.findall("[A-Z]+","AAaSAZsasEdsDddBDsSa"))

print(re.sub("a","A",r"assdadsc\bnas\d\aff",3))#用A替换a,替换三次，不写数字全部替换

# 被比较字符串前加上r，忽视转义字符影响