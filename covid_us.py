#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/08/27
判断美国现有确诊人数多少，是否少于5万，是就发邮件提醒
"""
from selenium import webdriver
from time import sleep
#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.PhantomJS()
#2.通过浏览器向服务器发送URL请求
browser.get("https://www.360kuai.com/mob/subject/400?sign=360_6aa05217&stab=2&whprovince=america")
#sleep(3)
#3.刷新浏览器
#browser.refresh()
#4.设置浏览器的大小
browser.set_window_size(1400,800)

#5.设置链接内容
#element=browser.find_element_by_link_text("每周")
#element=browser.find_element_by_xpath("//li[@data-period='week']") #每周


#element.click()
element=browser.find_element_by_class_name("wh-info-item-diff")
increase=browser.find_element_by_class_name("wh-info-item-diff").find_elements_by_tag_name("span")[-1]#相较上日变动额
increase=int(increase.text)
#判断较上日变动
if increase>0:
    print("美国现存确诊正常增加")


else :
    print("美国现存确诊减少,相较上日：",increase)
#判断现有确诊总数
illness=browser.find_element_by_class_name("wh-info-item-count-num") #现有确诊
illness=int(illness.text)
if illness>200000:
    print("美国现存确诊大于20万，当前为",illness)
elif illness>100000:
    print("美国现存确诊大于10万，当前为", illness)
elif illness > 50000:
    print("美国现存确诊大于5万，当前为", illness)
elif illness < 50000:
    print("警告：美国现存确诊小于于5万，当前为", illness)
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

    message = MIMEText('美股可能回调', 'plain', 'utf-8')  # 正文
    message['From'] = Header("叶志豪", 'utf-8')  # 发信人
    message['To'] = Header("叶志豪", 'utf-8')  # 收信人

    subject = "警告：美国现存确诊小于于5万"+str(illness)
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 587)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
#无头 可用
browser.close()#关闭浏览器
