#coding=utf-8
import requests
from bs4 import BeautifulSoup

url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
rsp = requests.get(url)
rsp.encoding = 'utf-8'
print(rsp.encoding)
with open('D:/demo.html', 'w', encoding='utf-8') as f:
    f.write(rsp.text)