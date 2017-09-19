import json
import re
import random
import time
import requests
from pymongo import MongoClient


def run():
    gzlist = ['ImportNew']  # 公众号

    url = 'https://mp.weixin.qq.com'
    # 设置请求头参数
    header = {
        "HOST": "mp.weixin.qq.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0"
    }

    # 读取文件中的cookie参数
    with open('cookie.txt', 'r', encoding='utf-8') as f:
        cookie = f.read()
    cookies = json.loads(cookie)
    response = requests.get(url=url, cookies=cookies)
    token = re.findall(r'token=(\d+)', str(response.url))[0]  # 获取链接中令牌
    # 存储数据字典
    lis = []
    # 设置请求参数
    for query in gzlist:
        query_id = {
            'action': 'search_biz',
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'query': query,
            'begin': '0',
            'count': '5',
        }
        search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
        search_response = requests.get(search_url, cookies=cookies, headers=header, params=query_id)
        lists = search_response.json().get('list')[0]
        fakeid = lists.get('fakeid')  # 获取链接中fakeid参数，用做请求参数
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '0',
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
        }
        appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
        appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
        max_num = appmsg_response.json().get('app_msg_cnt')  # 总条数
        num = int(int(max_num) / 5)  # 每页显示5条数据，算出总页数进行遍历，进行翻页
        begin = 0
        while num + 1 > 0:
            query_id_data = {
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'random': random.random(),
                'action': 'list_ex',
                'begin': '{}'.format(str(begin)),
                'count': '5',
                'query': '',
                'fakeid': fakeid,
                'type': '9'
            }
            print('第%s页' % (begin))
            query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
            fakeid_list = query_fakeid_response.json().get('app_msg_list')
            # 遍历获取到的文章
            for item in fakeid_list:
                datas = {}
                title = item.get('title')
                datas['title'] = title #文章标题
                href = item.get('link')
                datas['href'] = href #文章的链接
                lis.append(datas) #添加到列表中
            num -= 1
            begin = int(begin)
            begin += 5
            time.sleep(2)
    return lis


def sava_mg(lis):
    '''
    数据入库
    '''
    client = MongoClient('mongodb://localhost:27017')
    db = client.pythondb
    test = db.test
    test.insert(lis)
    client.close()


def main():
    '''
    程序入口
    :return:
    '''

    lis = run()
    sava_mg(lis)

if __name__ == '__main__':
    main()