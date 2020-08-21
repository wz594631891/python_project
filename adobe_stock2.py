from selenium import webdriver

from time import sleep

#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.Chrome()

#2.通过浏览器向服务器发送URL请求
browser.get("https://m.cn.investing.com/equities/adobe-sys-inc-technical")
sleep(3)


#3.刷新浏览器
#browser.refresh()

#4.设置浏览器的大小
browser.set_window_size(1400,800)

#5.设置链接内容
#element=browser.find_element_by_link_text("每周")
element=browser.find_element_by_xpath("//li[@data-period='week']") #每周


element.click()
element=browser.find_element_by_class_name("coloredBox")
print(element.text) #强力买入 可用
browser.close()#关闭浏览器
