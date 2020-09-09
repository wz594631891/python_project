#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/09/09 -
自动卖出华安纳斯达克（未完成
"""

from selenium import webdriver

from time import sleep

#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
driver = webdriver.Chrome()

#2.通过浏览器向服务器发送URL请求
driver.get("https://trade.1234567.com.cn/FundtradePage/redemption?spm=l") #卖基金页面

#sleep(3)


#3.刷新浏览器
#driver.refresh()

#4.设置浏览器的大小
driver.set_window_size(1400,800)

##2.1 可能登陆页面
# 打开文件
#2.1.1读取用户名和密码 ok
f = open("E:\\username.txt","r")   #设置文件对象
username= f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭
f = open("E:\\password.txt","r")   #设置文件对象
password= f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭

driver.find_element_by_css_selector("#tbname").send_keys(username)
driver.find_element_by_css_selector("#tbpwd").send_keys(password)
driver.find_element_by_css_selector("#btn_login").click()

#5.设置链接内容
#element=driver.find_element_by_link_text("每周")
#element=driver.find_element_by_css_selector(".summary > span")


#element.click()
#element=driver.find_element_by_class_name("coloredBox")
#print(element.text) #强力买入 可用
driver.close()#关闭浏览器
