#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#@Author:SenYang
#@Time:2021/7/19 9:09
#@File:spider.py
#@Software:PyCharm

import sys
import os

from bs4 import BeautifulSoup  #网页解析，获取数据
import re   #正则，文字匹配
import urllib.request,urllib.error#制定URL，获取网络资源
import xlwt     #进行excel操作
import sqlite3  #进行数据库操作

'''
数据库操作失败
'''

def main():
    baseurl="https://movie.douban.com/top250?start="
    # 1,爬取网页,逐一数据解析
    datalist=getData(baseurl)


    # 3,保存数据
    dbpath="movie.db"
    savepath="./豆瓣电影Top250.xls"#当前文件夹下    “.\\”文件系统
    saveData(datalist,savepath)
    saveData2DB(datalist,dbpath)
    #askURL("https://movie.douban.com/top250?start=")
    #print("hello")


#影片详情页链接匹配规则
findLink=re.compile(r'<a href="(.*?)">') #创建正则对象，表示字符串规则
#影片图片链接匹配规则
findImgSrc=re.compile(r'<img.*src="(.*?)" width=',re.S) #忽略换行符
#影片片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数
findJudge=re.compile(r'<span>(\d*)人评价</span>')
#影片概括
findInq=re.compile(r'<span class="inq">(.*)</span>')
#找到影片相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)#忽视换行符


#爬取网页
def getData(baseurl):
    datalist=[]

    for i in range(0,10):
        url=baseurl+str(i*25)   #调用获取页面信息函数，一共十次
        html=askURL(url)        #保存获取到的网页源码
        # 逐一解析数据
        soup=BeautifulSoup(html,"html.parser")

        for item in soup.find_all('div',class_="item"):#查找符合要求的字符串
           #print(item)
            data=[]#保存一部电影的全部信息
            item=str(item)
          #  print(item)

            #获取影片详情链接
            link=re.findall(findLink,item)[0]
            data.append(link)

            imgSrc=re.findall(findImgSrc,item)[0]#添加图片
            data.append(imgSrc)

            titles=re.findall(findTitle,item)#
            if (len(titles)==2):
                ctitle=titles[0]#中文名
                data.append(ctitle)
                otitle=titles[1].replace("/","") #外文名，并去掉/
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append('')#留空，占位

            rating=re.findall(findRating,item)[0]#评分
            data.append(rating)

            judgeNum=re.findall(findJudge,item)[0]#评价人数
            data.append(judgeNum)

            inq=re.findall(findInq,item)#添加概述，考虑没有概括的电影
            if(len(inq)!=0):
                data.append(inq[0].replace("。",""))
            else:
                data.append(" ")#留空

            bd=re.findall(findBd,item)[0]
            re.sub('<br(\s+)?/>(\s+)?'," ",bd)#去掉<br/>
            re.sub('/'," ",bd)#去掉/
            data.append(bd.strip())#去掉前后空格
            datalist.append(data)#把处理好的一部电影信息放入datalist
 #   print(datalist)
    return datalist

#得到一个指定URL的网页内容
def askURL(url):
    #模拟浏览器头部信息，向豆瓣服务器发送消息
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    #用户代理，告诉豆瓣服务器我们是什么类型的机器，浏览器
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
       # print(html)
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)  # 创建工作表
    col=("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概括","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])#列名
    for i in range(0,250):
        print("第%d条写入"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)  # 保存数据表
    print("success save data in excel ")

def saveData2DB(datalist,dbpath):
    print("-"*20)
    init_db(dbpath)
    conn=sqlite3.connect(dbpath)
    cur=conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index==4 or index==5:
                continue
            data[index]='"'+data[index]+'"'
        sql='''
            insert into movie250(
            info_link,pic_link,cname, ename, score, rated,instruction,info)
            values(%s)''' %",".join(data)
       # print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()
    print("成功保存到数据库！")



#创建数据库
def init_db(dbpath):
    if os.path.exists(dbpath):
        os.remove(dbpath)
    sql='''
    create table movie250(
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar,
    ename varchar,
    score numeric,
    rated numeric,
    instruction text,
    info text    
    )    
    '''
    conn=sqlite3.connect(dbpath)#创建连接
    cursor=conn.cursor()#获取游标
    cursor.execute(sql)#执行语句

    conn.commit()#提交更改
    conn.close()#关闭数据库


if __name__ =="__main__": #当程序执行时
    main()
    print("爬取完毕！")
    #调用函数

