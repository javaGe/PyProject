#coding=utf-8
'''
数据分析：
从以下维度进行分析：

观众的地理位置分布
观众的评论日期时间分布
观众的评分情况
以及电影评论的词云图

使用的技术:
分析： pandas 和collections 库
分词：jieba
可视化: pyecharts
'''


import pandas as pd
from collections import Counter
from pyecharts import Map, Geo, Bar
import jieba
import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import snownlp
from PIL import Image
import numpy as np



def read_csv(filename, titles):
    comments = pd.read_csv(filename, names=titles)
    return comments


def draw_map(comments):
    try:
        attr = comments['cityName'].fillna("zero_token")
        data = Counter(attr).most_common(100)
        #data.remove(data[data.index([(i, x) for i, x in (data) if i == 'zero_token'][0])])

        geo = Geo("《毒液》观众位置分布", "数据来源：猫眼电影 - SmartCrane采集", title_color="#fff", title_pos="center", width=1000,
                  height=600, background_color='#404a59')
        attr, value = geo.cast(data)
        geo.add("", attr, value, visual_range=[0, 1000], maptype='china', visual_text_color="#fff", symbol_size=10,
                is_visualmap=True)
        geo.render("./观众位置分布-地理坐标图.html")  # 生成html文件
        geo  # 直接在notebook中显示
    except Exception as e:
        print(e)


def draw_bar(comments):
    data_top20 = Counter(comments['cityName']).most_common(20)
    bar = Bar('《毒液》观众来源排行TOP20', '数据来源：猫眼-Ryan采集', title_pos='center', width=1200, height=600)
    attr, value = bar.cast(data_top20)
    bar.add('', attr, value, is_visualmap=True, visual_range=[0, 3500], visual_text_color='#fff', is_more_utils=True,
            is_label_show=True)
    bar.render('./观众来源排行-柱状图.html')
    print("success")


def draw_wordCloud(comments):
    data = comments['content']

    comment_data = []

    for item in data:
        if pd.isnull(item) == False:
            comment_data.append(item)

    # print(comment_data)
    comment_after_split = jieba.cut(str(comment_data), cut_all=False)
    words = ' '.join(comment_after_split)

    # c=Counter(words).most_common()
    # print(c)

    stopwords = STOPWORDS.copy()
    stopwords.add('电影')
    stopwords.add('一部')
    stopwords.add('一个')
    stopwords.add('没有')
    stopwords.add('什么')
    stopwords.add('有点')
    stopwords.add('感觉')
    stopwords.add('毒液')
    stopwords.add('就是')
    stopwords.add('觉得')

    wc = WordCloud(width=1080, height=960, background_color='white', font_path='STKAITI.TTF', stopwords=stopwords,
                   max_font_size=400, random_state=50)
    wc.generate_from_text(words)

    plt.figure(figsize=(10, 8))
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig('./WordCloud.png')
    plt.show()


def draw_DateBar(comments):
    time = comments['startTime']
    timeData = []
    for t in time:
        if pd.isnull(t) == False:
            date = t.split(' ')[0]
            timeData.append(date)

    data = Counter(timeData).most_common()
    data = sorted(data, key=lambda data: data[0])
    # 由于数据中有两个 11月8日 的数据，不应该出现在我们的数据中，故删去
    del data[0]

    print(data)

    bar = Bar('《毒液》观众评论数量与日期的关系', '数据来源：猫眼电影-SmartCrane采集', title_pos='center', width=1200, height=600)
    attr, value = bar.cast(data)
    bar.add('', attr, value, is_visualmap=True, visual_range=[0, 3500], visual_text_color='#fff', is_more_utils=True,
            is_label_show=True)
    bar.render('./观众评论日期-柱状图.html')
    print("success")


def draw_TimeBar(comments):
    time = comments['startTime']
    timeData = []
    for t in time:
        if pd.isnull(t) == False:
            time = t.split(' ')[1]
            hour = time.split(':')[0]
            timeData.append(hour)

    data = Counter(timeData).most_common()
    data = sorted(data, key=lambda data: data[0])
    # 由于数据中有一个 11月15日 的数据，不应该出现在我们的数据中，故删去
    # del data[0]
    print(data)

    bar = Bar('《毒液》观众评论数量与时间的关系', '数据来源：猫眼电影-SmartCrane采集', title_pos='center', width=1200, height=600)
    attr, value = bar.cast(data)
    bar.add('', attr, value, is_visualmap=True, visual_range=[0, 3500], visual_text_color='#fff', is_more_utils=True,
            is_label_show=True)
    bar.render('./观众评论时间-柱状图.html')
    print("success")


if __name__ == "__main__":
    filename = "./comments.csv"
    titles = ['nickName', 'cityName', 'content', 'score', 'startTime']
    comments = read_csv(filename, titles)
    print(comments.head(5))
    # draw_map(comments)
    # draw_bar(comments)
    # draw_wordCloud(comments)
    # draw_DateBar(comments)
    # draw_TimeBar(comments)
    print('success!!')