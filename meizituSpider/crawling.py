#coding=utf-8
import os
import datetime
import random
from pymongo import MongoClient


import requests
from bs4 import BeautifulSoup

'''
爬取妹子图的类
'''
class Meizitu:
    #初始化请求头，user_agent
    def __init__(self):
        self.headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"}
        client = MongoClient()
        db = client['mztdb']
        self.mzt_col = db['mzt']
        self.title = '' #存储标题
        self.url = '' #存储页面链接
        self.img_urls = [] #存储图片url

    #发送请求获取response
    def request(self, url):
        rsp = requests.get(url, params=self.headers)
        return rsp

    #获取所有套图url
    def get_all_url(self, url):
        rep = self.request(url)
        # print(rep.text)
        bs = BeautifulSoup(rep.text, 'lxml')
        all_a = bs.find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text() #套图的标题
            path = title.replace('?', '-') #文件名称
            print('套图名称：',path)
            self.makedir(path) #创建文件夹
            href = a['href'] #套图url
            if self.mzt_col.find_one('套图url',href):
                print('该套图已经采集过')
            else:
                self.get_page_url(href) #获取套图中的url

    #解析url，获取页面图片url
    def get_page_url(self, href):
        print("获取页面的url")
        rsp = self.request(href) #请求套图url
        self.headers['referer'] = href #设置网页来源头，破解防盗链
        bs = BeautifulSoup(rsp.text, 'lxml')
        #获取也页数
        max_page = bs.find('div', class_='pagenavi').find_all('span')[-2].get_text()
        #分页
        for page in range(1, int(max_page)+1):
            img_url = href+'/'+str(page) #获取每一页url
            #print(img_url)
            self.get_imge_url(img_url) #获取图片url

    #获取每张图片url
    def get_imge_url(self, page_url):
        print('获取每一页的url')
        rsp = self.request(page_url)
        bs = BeautifulSoup(rsp.text, 'lxml')
        #获取每张图片的url
        img_url = bs.find('div', class_='main-image').find('img')['src']
        #保存
        self.save_image(img_url, page_url)

    #保存图片
    def save_image(self, img_url, page_url):
        print('保存图片')
        img = self.requestpic(img_url, page_url)
        name = img_url[-9:-4] #图片命名
        with open(name+'.jpg', 'ab' ) as f:
            f.write(img.content) #将二进制数据写入文件中

    '''
    该方法用于破解防盗链，加多一个referer,不加的话图片下载无法打开
    '''
    def requestpic(self, url, Referer):  ##这个函数获取网页的response 然后返回
        user_agent_list = [ \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        ua = random.choice(user_agent_list)
        headers = {'User-Agent': ua, "Referer": Referer}  ##较之前版本获取图片关键参数在这里
        content = requests.get(url, headers=headers)
        return content

    #创建保存图片的文件夹
    def makedir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join('D:\\mzt', path))#判断文件是否存在
        if not isExists:
            os.makedirs(os.path.join('D:\\mzt', path))  #创建文件
            os.chdir(os.path.join('D:\\mzt', path)) #切换到该目录
            return True
        else:
            print('文件已存在')
            return False

mzt = Meizitu()
mzt.get_all_url("http://www.mzitu.com/all/")
