#!/usr/bin/python3
# coding:utf-8
"""
@author 叶志豪2020
@date 2020/09/09
抓新浪新闻标题 ok
"""

from selenium import webdriver

from time import sleep

#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
driver = webdriver.PhantomJS()

#2.通过浏览器向服务器发送URL请求
driver.get("https://news.sina.com.cn/world/") #

#sleep(3)


#3.刷新浏览器
#driver.refresh()

#4.设置浏览器的大小
driver.set_window_size(1400,800)

##2.1 可能登陆页面
# 打开文件
#2.1.1读取用户名和密码 ok

elements=driver.find_elements_by_css_selector("a[target='_blank']")
for element in elements:
    str=element.text
    str=str.replace("评论","") #替换
    str = str.replace("详细", "")
    print(str)
#5.设置链接内容
#element=driver.find_element_by_link_text("每周")
#element=driver.find_element_by_css_selector(".summary > span")


#element.click()
#element=driver.find_element_by_class_name("coloredBox")
#print(element.text) #强力买入 可用
driver.close()#关闭浏览器
