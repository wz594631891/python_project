from selenium import webdriver

from time import sleep

#1.创建Chrome浏览器对象，这会在电脑上在打开一个浏览器窗口
browser = webdriver.PhantomJS()

#2.通过浏览器向服务器发送URL请求
browser.get("http://news.sina.com.cn/world/")
#sleep(3)


#3.刷新浏览器
#browser.refresh()

#4.设置浏览器的大小
browser.set_window_size(1400,800)

#5.设置链接内容
#element=browser.find_element_by_link_text("每周")
# element=browser.find_element_by_css_selector(".summary > span")
elements=browser.find_elements_by_xpath("//a[@target='_blank']") #
#while循环
i=0
sum=0
while i<=len(elements)-1:
     print(elements[i].text)


#element.click()
#element=browser.find_element_by_class_name("coloredBox")
# print(elements.text) #强力买入 可用
browser.close()#关闭浏览器
