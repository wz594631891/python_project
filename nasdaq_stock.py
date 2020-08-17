#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/08/17
判断nasdaq买入卖出信号指标是否改变，是则发送邮件 （日周期）
"""
from bs4 import BeautifulSoup
import requests


url = 'https://m.cn.investing.com/indices/nq-100-technical'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'} #反反爬虫
r = requests.get(url,headers=headers) #反反爬虫
demo = r.text  # 服务器返回响应

from simplified_scrapy.simplified_doc import SimplifiedDoc
doc = SimplifiedDoc(demo)
str=doc.getElementsByTag("td")[-1].getChild().text #抓取元素

## 读取文件
f = open("data3.txt","r")   #设置文件对象
data = f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭
if data!=str:
    ## 发送邮件
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    # 第三方 SMTP 服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="2460307574"    #用户名
    mail_pass="mbygawjmypcydhii"   #口令


    sender = '2460307574@qq.com'
    receivers = ['2460307574@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText('nasdaq评价', 'plain', 'utf-8') #正文
    message['From'] = Header("叶志豪", 'utf-8') #发信人
    message['To'] =  Header("叶志豪", 'utf-8') #收信人

    subject = str
    message['Subject'] = Header(subject, 'utf-8')


    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
    ## 写入文件

    with open('data3.txt','w') as f:    #设置文件对象
         f.write(str)                 #将字符串写入文件中

else:
    print("评价结果相同")
