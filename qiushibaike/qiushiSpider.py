# coding=utf-8
from lxml import etree
from bs4 import BeautifulSoup
from pymongo import MongoClient

import requests
import time
import queue
import json
import threading
import traceback


class thread_crawl(threading.Thread):
    '''
    抓取页面线程类，创建多线程，然后从队列中获取页码进行抓取
    '''

    def __init__(self, thread_ID, q):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID  # 线程id
        self.q = q  # 初始化队列

    def run(self):
        print('thread_crawl starting %s ' % self.thread_ID)
        self.qiushi_spider()
        print('thread_crawl exiting %s' % self.thread_ID)

    def qiushi_spider(self):
        while True:
            if self.q.empty():  # 判读队列是否为空
                break
            else:
                page = self.q.get()  # 获取页码
                # 目标网页
                url = 'http://www.qiushibaike.com/hot/page/' + str(page) + '/'
                # 请求头，模拟浏览器
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                    'Accept-Language': 'zh-CN,zh;q=0.8'
                }

                # 多次请求失败时结束，防止死循环
                timeout = 4
                while timeout > 0:
                    timeout -= 1
                    try:
                        content = requests.get(url, headers=headers)
                        html_queue.put(content.text)
                        break
                    except Exception as e:
                        ex_str = traceback.format_exc()
                        print(ex_str)


class thread_parser(threading.Thread):
    '''
    html页面解析类
    '''

    def __init__(self, thread_ID, queue, lock, f):
        '''
        初始化
        :param thread_ID: 线程id
        :param queue: 存储html的队列
        :param lock: 线程锁
        :param f: 文件操作，用于将解析页面内容写入硬盘
        '''
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID
        self.queue = queue
        self.lock = lock
        self.f = f

    def run(self):
        print('thread_parser starting %s' % self.thread_ID)
        global total, exitFlag
        while not exitFlag:
            try:
                '''
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且block为False，队列将引发Empty异常。
                '''
                item = self.queue.get(False)  # 获取html页面
                if not item:
                    pass
                self.html_parser(item)
                self.queue.task_done()
            except:
                pass

    def html_parser(self, item):
        '''
        解析网页，获取内容
        :param item: 网页
        :return:
        '''
        global total
        try:
            # html = etree.HTML(item)  #
            html = BeautifulSoup(item, 'lxml')
            result_div = html.find(id='content-left')
            if result_div is not None:
                for article_div in result_div.find_all(class_='article'):
                    content = article_div.find(class_='content').get_text().strip() # 获取文章内容
                    save(content)
                    print(content)

            # print(result_div)
            # result = html.find('//div[contains(@id,"qiushi_tag")]')
            # for site in result:
            #     try:
            #         imgUrl = site.xpath('.//img/@src')[0]
            #         title = site.xpath('.//h2')[0].text
            #         content = site.xpath('.//div[@class="content"]')[0].text.strip()
            #         print(content)
            #         vote = None
            #         comments = None
            #         try:
            #             vote = site.xpath('.//i')[0].text
            #             comments = site.xpath('.//i')[1].text
            #         except:
            #             pass
            #         result = {
            #             'imgUrl': imgUrl,
            #             'title': title,
            #             'content': content,
            #             'vote': vote,
            #             'comments': comments,
            #         }
            #
            #         with self.lock:  # 这里的意思是加锁和释放锁
            #             print('write %s' % json.dumps(result))
            #             # self.f.write(json.dumps(result, ensure_ascii=False).encode('utf-8') + "\n")
            #
            #     except Exception as e:
            #         ex_str = traceback.format_exc()
            #         print(ex_str)
        except Exception as e:
            ex_str = traceback.format_exc()
            print(ex_str)
        with self.lock:
            total += 1  # 记录页面的数量


def save(content):
    try:
        client = MongoClient('localhost', 27017)
        db = client.pythondb
        coll = db.qiushi
        data = {'content':content}
        coll.save(data)
        print('insert success')
    except Exception as e:
        print(e)
    finally:
        client.close()
html_queue = queue.Queue()  # 存储页面的队列
exitFlag = False # 用于通知线程是否退出
lock = threading.Lock()  # 获取锁
total = 0 # 记录页面


def main():
    output = open('qiushi.json', 'a')  # 记录内容文件

    # 初始化网页页码page从1-10个页面
    pageQueue = queue.Queue(50)
    for page in range(1, 11):
        pageQueue.put(page)

    # 初始化采集线程
    crawlThreads = []  # 存储线程
    crawList = ['crawl-1', 'crawl-2', 'crawl-3']  # 线程名称

    for threadID in crawList:
        thread = thread_crawl(threadID, pageQueue) # 采集线程
        thread.start() # 启动线程
        crawlThreads.append(thread) # 添加到集合中

    # 初始化页面解析线程
    parserThreads = []
    parserList = ['parser-1', 'parser-2', 'parser-3']

    for threadID in parserList:
        # 创建解析线程
        thread = thread_parser(threadID, html_queue, lock, output)
        thread.start()
        parserThreads.append(thread)

    # 等待页码队列清空
    while not pageQueue.empty():
        pass

    # 等待所有采集线程执行完成，再继续往下执行
    for t in crawlThreads:
        t.join()

    # 等待页面队列清空
    while not html_queue.empty():
        pass

    # 当页面队列为空时，通知线程退出处理页面
    global exitFlag
    exitFlag = True

    # 等待页面处理线程全部结束
    for t in parserThreads:
        t.join()

    output.close()
    print('exiting main thread')


if __name__ == '__main__':
    main()