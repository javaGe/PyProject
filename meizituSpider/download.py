# -*- coding=utf-8 -*-
import random

import requests
import time

from proxyIP import get_IP
from proxyIP import check_IP
from meizituSpider import user_agent
import re


class download():
    def __init__(self):
        '''
        初始化代理IP列表和用户代理
        '''
        # get_IP.getIP(1)
        # check_IP.check()
        self.iplist = []  # 初始化一个IP列表
        with open('valid_ip.csv', 'r', encoding='utf-8') as r:
            lines = r.readlines()  # 读取所有行
            for line in lines:
                ip = re.sub(r'\n', '', line)
                if ip == '':
                    continue
                self.iplist.append(ip)
                # print(self.iplist)
        self.user_agent_list = user_agent.UA  # 用户代理列表

    def get(self, url, timeout, proxy=None, num_req=6):
        '''
        :param url: 请求链接
        :param timeout:  超时时间
        :param proxy:  代理IP 默认为None
        :param num_req: 请求次数
        :return:
        '''
        UA = random.choice(self.user_agent_list)  # 获取随机用户代理
        headers = {'User-Agent': UA}  # 构造代理头
        if proxy == None:  # 代理为空时
            try:
                return requests.get(url, headers=headers, timeout=timeout)
            except:  # 请求出现异常时，继续按照设定的次数进行请求
                if num_req > 0:
                    time.sleep(5)
                    print('获取页面出错，请求第%s次' % (num_req))
                    return self.get(url, timeout, num_req=num_req - 1)  # 继续调用请求
                else:
                    print('使用代理。。。')
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': IP}
                    return self.get(url, timeout, proxy)
        else:  # 代理不为空时
            try:
                IP = ''.join(str(random.choice(self.iplist)).strip())
                proxy = {'http': IP}
                return requests.get(url, headers=headers, proxys=proxy, timeout=timeout)
            except: #更换代理
                if num_req > 0:
                    time.sleep(10)
                    IP = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {"http": IP}
                    print('正在更换代理，请求第%s次' %(num_req))
                    print('当前代理为：%s' %(IP))
                    return self.get(url, timeout, proxy, num_req-1)
                else: #退出代理
                    print('代理也不好使')
                    return

dw = download() #实例化
print(dw.get('http://mzitu.com', 3))