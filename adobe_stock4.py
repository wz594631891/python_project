#-*-  coding:utf-8 -*-
#主要用来测试selenium使用phantomJs

#导入webdriver
from selenium import webdriver
import time

#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

#调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()
driver.set_window_size(1366, 768)
#如果没有在环境变量指定PhantomJS位置
#driver = webdriver.PhantomJS(executable_path = "./phantomjs")

#get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)

driver.get("http://www.baidu.com/")

#获取页面名为wraper的id标签的文本内容
#data = driver.find_element_by_id('wrapper').text
data = driver.find_element_by_css_selector('#wrapper').text

#打印数据内容
print(data)