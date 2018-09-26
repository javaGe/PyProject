#coding=utf-8
import requests
import time
import os
from bs4 import BeautifulSoup
from meizituSpider import download
'''
小说太古神王爬取
url：http://www.60355.com/0_202/
'''

class LiuLing():
    def __init__(self):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
        self.path = 'D:/stroy/总裁贴身兵王/'
        self.makedir(self.path)  # 创建文件夹

    def request(self, url):
        '''
        请求网站
        :param url: 请求url
        :return:
        '''
        rsp = requests.get(url, headers=self.headers)
        rsp.encoding = 'gbk'
        return rsp

    def get_title_url(self, url):
        '''
        获取所有标题链接
        :param url: 小说链接，通过该链接可以获取所有章节链接
        :return:
        '''
        # rsp = self.request(url) #请求网页
        rsp = download.request.get(url=url, timeout=5)
        rsp.encoding = 'gbk'
        # print(rsp.text)
        soup = BeautifulSoup(rsp.text, 'lxml')
        dds = soup.find('div', id='list').find_all('dd')[570:] #获取所有的标题
        site = 'http://www.60355.com' #网站链接
        for dd in dds:
            time.sleep(5)
            title = dd.get_text().strip() #获取标题
            title_url = dd.find('a')['href'] #获取标题url
            # print(title+">>"+title_url)
            self.get_title_text(site+title_url, title) #获取每个标题的内容

    def get_title_text(self, url, title):
        '''
        获取每个章节的内容
        :param url: 章节url
        :param title:  章节
        :return:
        '''
        # rsp = self.request(url) #发送请求
        rsp = download.request.get(url, timeout=5) #使用代理
        rsp.encoding = 'gbk'
        soup = BeautifulSoup(rsp.text, 'lxml')
        content = soup.find('div', id='content').get_text()
        print(title)
        with open(self.path+title+'.txt', 'w', encoding='utf-8') as w:
            w.write(content)


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



ll = LiuLing()
ll.get_title_url(url='http://www.60355.com/12_12799/')