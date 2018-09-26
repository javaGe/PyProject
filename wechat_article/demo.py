import re

import time
from selenium import webdriver
from bs4 import BeautifulSoup

# rsp = 'https://mp.weixin.qq.com/cgi-bin/home?t=home/index&lang=zh_CN&token=1500943863'
# token = re.findall(r'token=(\d+)', rsp)[0]
import requests
from selenium.webdriver.common.by import By
#
# url = "http://ueditor.baidu.com/website/examples/completeDemo.html"
# rsp = requests.get(url)
# browser= webdriver.Chrome()
# browser.get(url)
# browser.find_element(By.CSS_SELECTOR, '#edui135_body > div.edui-box.edui-icon.edui-default').click()
# time.sleep(5)
# browser.quit()

# print(token)

# from pymongo import MongoClient as mc
#
# clicent = mc('mongodb://localhost:27017')
# db = clicent.pythondb
# test = db.test
# users = [{'name':'ggf', 'age':22, 'job':'coder'},{'name':'ggf', 'age':22, 'job':'coder'},{'name':'ggf', 'age':22, 'job':'coder'},{'name':'ggf', 'age':22, 'job':'coder'}]
# test.insert(users)

url = "https://mp.weixin.qq.com/s?__biz=MjM5NzMyMjAwMA==&mid=2651479108&idx=1&sn=68aa65954edc041b86d1d8f7501210b6&chksm=bd25303b8a52b92dacece808204a77816789ae85809bc22d5500a6750c30ed6504006270c87d&scene=21#wechat_redirect"
rsp = requests.get(url)
soup =  BeautifulSoup(rsp.text, 'lxml')
text = soup.find(id='activity-name').get_text()
content = soup.find(class_='rich_media_content ')
print(text.strip())
print(content)