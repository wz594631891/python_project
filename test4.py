from bs4 import BeautifulSoup
import requests


url = 'https://cn.investing.com/equities/adobe-sys-inc-technical'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'} #反反爬虫
r = requests.get(url,headers=headers) #反反爬虫
demo = r.text  # 服务器返回响应
print(type(demo))