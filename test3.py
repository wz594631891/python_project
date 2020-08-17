## 读取文件
f = open("data.txt","r")   #设置文件对象
str = f.read()     #将txt文件的所有内容读入到字符串str中
f.close()   #将文件关闭
## 提取中文
import re
m = re.findall('[\u4e00-\u9fa5]+', str)
print(m)

## 写入文件
str=repr(m)
with open('data.txt','w') as f:    #设置文件对象
     f.write(str)                 #将字符串写入文件中