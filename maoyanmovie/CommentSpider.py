# coding=utf-8

'''
爬出猫眼电影中《毒液》的评论信息，进行数据分析
URL：http://m.maoyan.com/movie/42964/comments?_v_=yes

分析维度：
1.用户昵称
2.所在城市
3.评论内容
4.电影评分
5.评论时间

'''
import json
import time
import datetime
import requests
import pandas as pd

def get_data(url):
    '''
    通过URL访问网页，获取返回的数据
    URL：http://m.maoyan.com/movie/42964/comments?_v_=yes
    请求参数：offset=0
    startTime：评论的时间  可以通过上映的时间和评论的时间进行比较，然后循环遍历进行数据采集
    '''

    # 设置请求头信息
    headers = {
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }

    try:
        # 请求目标网站
        r = requests.get(url=url, headers=headers)
        # 通过该方法判断是否请求成功，如果status_code不为200时，就会抛出异常
        r.raise_for_status()
        # 请求成功后，返回响应数据
        return r.text

    except requests.HTTPError as e:
        print(e)
        print('HTTPError')
    except requests.RequestException as e:
        print(e)
    except:
        print('UnKnown Error!')


def parse_data(data):
    '''
    解析获取到的数据，获取需要的字段
    1.用户昵称
    2.所在城市
    3.评论内容
    4.电影评分
    5.评论时间
    :param html: 获取到的json数据
    :return:
    '''

    # 获取我们需要的数据
    json_data = json.loads(data)['cmts']

    # 定义一个数组，用来存储解析的数据
    comments = []

    try:
        # 遍历json数据
        for item in json_data:
            comment = []
            # 用户昵称
            comment.append(item['nickName'])
            # 所在城市
            comment.append(item['cityName'] if 'cityName' in item else '')
            # 评论内容
            comment.append(item['content'])
            # 电影评分
            comment.append(item['score'])
            # 评论时间
            comment.append(item['startTime'])

            # 将遍历的数据添加到数组中
            comments.append(comment)

        return comments

    except Exception as e:
        print(comment)
        print(e)



def save_data(comments):
    '''
    将解析后的数据进行存储（这里存储到文件中）
    :param comments:
    :return:
    '''

    file_name = './comments.csv'

    # 使用pandas将数据格式化后存储到文件中
    data_frame = pd.DataFrame(comments)
    data_frame.to_csv(file_name, mode='a', index=False, sep=',', header=False)

def main():
    '''
       功能：爬虫调度器，根据规则每次生成一个新的请求 url，爬取其内容，并保存到本地。
    '''

    # 获取当前时间，作为最新的评论时间
    start_time = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')
    end_time = '2018-12-01  00:00:00'  # 电影上映时间，评论爬取到此截至

    while start_time > end_time:
        url = 'http://m.maoyan.com/mmdb/comments/movie/42964.json?_v_=yes&offset=0&startTime=' + start_time.replace('  ', '%20')
        # 每次循环，需要将原来的变量清空
        data = None

        try:
            # 通过URL获取数据
            data = get_data(url)

        except Exception as e:
            time.sleep(1)
            data = get_data(url)

        else:
            time.sleep(2)

        # 解析获取到的数据
        comments = parse_data(data)
        # print(url)
        start_time = comments[14][4]
        print(start_time)

        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d  %H:%M:%S') + datetime.timedelta(seconds=-1)
        start_time = datetime.datetime.strftime(start_time, '%Y-%m-%d  %H:%M:%S')

        save_data(comments)

if __name__ == '__main__':
    main()
    print('end!!')