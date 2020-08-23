#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/08/21
判断华安纳斯达克100基金年化月收益是否大于15%（日周期）
"""
from bs4 import BeautifulSoup
import requests


url = 'http://fund.eastmoney.com/040046.html?spm=search'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'} #反反爬虫
r = requests.get(url,headers=headers) #反反爬虫
demo = r.text  # 服务器返回响应

from simplified_scrapy.simplified_doc import SimplifiedDoc
doc = SimplifiedDoc(demo)
#str=doc.getElementsByTag("td")[-1].getChild().text #抓取元素 最后一个
s=doc.getElementByClass("ui-font-middle ui-color-red ui-num")
s=s.getText()
#百分数转小数
num = float(s.strip('%')) # 去掉s 字符串中的 %
rate = num/100.0
rate=rate*12
if rate>0.15:
     percentage=str(rate*100) + '%' #小数转百分数
     print("华安纳斯达克100大于15%",percentage)
else:
     percentage = str(rate * 100) + '%'
     print("华安纳斯达克100小于15%",percentage)


