#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/09/12
判断广发纳斯达克基金是否限额超过一万
"""
from bs4 import BeautifulSoup
import requests


url = 'http://fund.eastmoney.com/270042.html?spm=search'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'} #反反爬虫
r = requests.get(url,headers=headers) #反反爬虫
demo = r.text  # 服务器返回响应

from simplified_scrapy.simplified_doc import SimplifiedDoc
doc = SimplifiedDoc(demo)

limit=doc.getElementsByClass("staticCell")[0].getChild().getText() #抓取购买限额
#获取数字
import re
number = re.sub("\D", "", limit)
number=int(number)
# print(number)
## 读取文件
f = open("E:\python_project\limit3_data.txt","r")   #设置文件对象
data = f.read()     #将txt文件的所有内容读入到字符串number中
f.close()   #将文件关闭
if data!=number and number>=10000:
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
    msg="当前为"+number
    message = MIMEText(msg, 'plain', 'utf-8') #正文
    message['From'] = Header("叶志豪", 'utf-8') #发信人
    message['To'] =  Header("叶志豪", 'utf-8') #收信人

    subject = "广发纳斯达克基金限额大于10000"
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



else:
    print("评价结果相同或限额未超10000,为"+str(number))
with open('E:\python_project\limit3_data.txt', 'w') as f:  # 设置文件对象
    f.write(str(number))  # 将字符串写入文件中



