#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/08/17
判断microsoft买入卖出信号指标是否改变，是则发送邮件 （日周期）
"""

from bs4 import BeautifulSoup
import requests
#list =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#for i in list:
url = 'https://www.manhuagui.com/comic/28765/463111.html#p=3'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}  # 反反爬虫
r = requests.get(url, headers=headers)  # 反反爬虫
demo = r.text  # 服务器返回响应

from simplified_scrapy.simplified_doc import SimplifiedDoc

doc = SimplifiedDoc(demo)
# str=doc.getElementsByTag("td")[-1].getChild().text #抓取元素
img = doc.getElementByClass("mangaFile").get("src") # 抓取元素 第一个
print(img)