#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@Author:SenYang
#@Time:2021/7/22 9:14
#@File:testSQL.py
#@Software:PyCharm

import sqlite3



#创建数据表
'''
conn=sqlite3.connect("test.db")#打开或者创建数据库文件
print("Open database successfully ")
c=conn.cursor()#获取游标

sql='''
    # create table company
    #     (id int primary key not null,
    #     name text not null,
    #     age int not null,
    #     address char(50),
    #     salary real);
'''

c.execute(sql)#执行语句


conn.commit() #提交数据库操作
conn.close()#关闭数据库连接
print("成功建表")
'''
#3插入数据
conn=sqlite3.connect("test.db")#打开或者创建数据库文件
print("Open database successfully ")
c=conn.cursor()#获取游标

# sql1='''
#     insert into company(id,name,age,address,salary)
#     values(1,'张三',32,'成都',8000)
# '''
#
# sql2='''
#     insert into company(id,name,age,address,salary)
#     values(2,'李四',28,'北京',8000)
# '''

sql="select id,name,address,salary from company"

cursor=c.execute(sql)#执行语句
for row in cursor:
    print("id=",row[0])
    print("name=",row[1])
    print("address=",row[2])
    print("salary=",row[3],"\n")

#c.execute(sql2)#执行语句

#conn.commit() #提交数据库操作
conn.close()#关闭数据库连接
print("成功查找")


#4查询数据




