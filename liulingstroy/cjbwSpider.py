import os

import requests
from bs4 import BeautifulSoup
import re


class Caojibw(object):
    def __init__(self):
        self.headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
        self.path = 'D:/stroy/超级兵王/'
        self.makedir(self.path)  # 创建文件夹

    def request(self, url):
        rsp = requests.get(url, headers=self.headers)
        rsp.encoding = 'gbk'
        return rsp

    def process(self, rsp):
        soup = BeautifulSoup(rsp.text, 'lxml')
        tds = soup.find('table').find_all('td')
        for td in tds:
            tag_a = td.find('a')
            if tag_a != None:
                title = tag_a.get_text().strip()
                href = tag_a['href']
                href = 'http://www.23us.com/html/10/10943/' + href
                print(title + '....' + href)
                self.get_content(title, href)

    def get_content(self, title, url):
        rsp = self.request(url)
        soup = BeautifulSoup(rsp.text, 'lxml')
        content = soup.find(id='contents').get_text().replace('\xa0', ' ')
        with open(self.path+title+'.txt', 'w', encoding='utf-8') as w:
            w.write(content)
        print('写入成功'+title)
    def makedir(self, path):
        '''
        保存小说的路径
        :param path: 文件夹路径
        :return:
        '''
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            print('文件夹已存在！')


cjbw = Caojibw()
url = 'http://www.23us.com/html/10/10943/'
rsp = cjbw.request(url)
cjbw.process(rsp=rsp)
