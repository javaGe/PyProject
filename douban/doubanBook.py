#coding=utf-8
'''
练习（一）爬取豆瓣读书
目标url：https://read.douban.com/columns/category/all
翻页的url：https://read.douban.com/columns/category/all?sort=hot&start=0
            https://read.douban.com/columns/category/all?sort=hot&start=10
'''

import urllib.request
from bs4 import BeautifulSoup
import time

#计数，计算书本的数量
num = 1
#开始时间
start_time = time.time()

url = 'https://read.douban.com/columns/category/all?sort=hot&start='
for i in range(0, 300, 10): # 这里的  range（初始，结束，间隔）
    # urllib.request库用来向该网服务器发送请求，请求打开该网址链接
    html = urllib.request.urlopen('https://read.douban.com/columns/category/all?sort=hot&start=%d' % i)
    # BeautifulSoup库解析获得的网页，第二个参数一定记住要写上‘lxml’，记住就行
    bsObj = BeautifulSoup(html, 'lxml')

    print('==============' + '第%d页' % (i / 10 + 1) + '==============')
    # 分析网页发现，每页有10本书，而<h4>标签正好只有10个。
    h4_node_list = bsObj.find_all('h4')  # 这里返回的是h4标签的list列表
    for h4_node in h4_node_list:  # 遍历列表
        # 获取h4标签内的a标签，但这里返回是只含1个元素的list
        a_node = h4_node.contents[0]
        title = a_node.contents[0]  # 因为是列表，要list[0]，取出来
        title = '<<' + title + '>>'
        print('第%d本书' % num, title)
        num = num + 1
    # 设置抓数据停顿时间为1秒，防止过于频繁访问该网站，被封
    time.sleep(1)

    end_time = time.time()
    duration_time = end_time - start_time
    print('运行时间共：%.2f' % duration_time + '秒')
    print('共抓到%d本书名' % num)

