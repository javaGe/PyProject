import datetime
import requests
import time

url = "http://www.baidu.com"
rep = requests.get(url)
#print(rep.text)
print(int(time.time()))