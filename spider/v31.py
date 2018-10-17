from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content,"lxml")
#bs自动转码
print("=="*12)
print(soup.head)
print("=="*12)
print(soup.meta)
print("=="*12)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
#也可以修改其中的内容，因为已经读到内存里了
soup.link.attrs["type"]="hahaha"
print(soup.link.attrs)

print(soup.name)
print(soup.attrs)