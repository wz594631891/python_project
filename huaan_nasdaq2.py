#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/08/23
判断华安纳斯达克100基金年五天内跌幅是否超过5%
"""
from bs4 import BeautifulSoup
import requests


url = 'https://m.cn.investing.com/indices/nq-100-historical-data'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'} #反反爬虫
r = requests.get(url,headers=headers) #反反爬虫
demo = r.text  # 服务器返回响应

from simplified_scrapy.simplified_doc import SimplifiedDoc
doc = SimplifiedDoc(demo)
#str=doc.getElementsByTag("td")[-1].getChild().text #抓取元素 最后一个
s=doc.getElementsByTag("tr")[1].getChildren()[-1].html#抓取元素 第1个
s2=doc.getElementsByTag("tr")[2].getChildren()[-1].html#抓取元素 第2个
s3=doc.getElementsByTag("tr")[3].getChildren()[-1].html#抓取元素 第3个
s4=doc.getElementsByTag("tr")[4].getChildren()[-1].html#抓取元素 第4个
s5=doc.getElementsByTag("tr")[5].getChildren()[-1].html#抓取元素 第5个
#百分数转小数
num = float(s.strip('%')) # 去掉s 字符串中的 %
num2 = float(s2.strip('%')) # 去掉s 字符串中的 %
num3 = float(s3.strip('%')) # 去掉s 字符串中的 %
num4 = float(s4.strip('%')) # 去掉s 字符串中的 %
num5 = float(s5.strip('%')) # 去掉s 字符串中的 %
#rate = num/100.0 + num2/100.0 +num3/100.0+ num4/100.0+num5/100.0
list=[num,num2,num3,num4,num5]
#while循环
i=0
sum=0
while i<=len(list)-1:
     sum+=list[i] #遍历过去五天内涨跌幅
     if sum < -5: #0.05 ->-5
          percentage = str(sum ) + '%'  # 小数转百分数
          print("华安纳斯达克100跌幅大于5%", percentage)
          ## 自动卖出

          ## 发送邮件
          import smtplib
          from email.mime.text import MIMEText
          from email.header import Header

          # 第三方 SMTP 服务
          mail_host = "smtp.qq.com"  # 设置服务器
          mail_user = "2460307574"  # 用户名
          mail_pass = "mbygawjmypcydhii"  # 口令

          sender = '2460307574@qq.com'
          receivers = ['2460307574@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

          message = MIMEText('华南纳斯达克跌幅超5%', 'plain', 'utf-8')  # 正文
          message['From'] = Header("叶志豪", 'utf-8')  # 发信人
          message['To'] = Header("叶志豪", 'utf-8')  # 收信人

          subject = "华安纳斯达克跌幅为"+percentage
          message['Subject'] = Header(subject, 'utf-8')

          try:
               smtpObj = smtplib.SMTP()
               smtpObj.connect(mail_host, 587)  # 25 为 SMTP 端口号
               smtpObj.login(mail_user, mail_pass)
               smtpObj.sendmail(sender, receivers, message.as_string())
               print("邮件发送成功")
          except smtplib.SMTPException:
               print("Error: 无法发送邮件")
     else:
          percentage = str(sum) + '%'
          print("华安纳斯达克100跌幅小于5")
     i+=1






