#coding=utf-8
'''
爬取8x8x网站的图片
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)

def init(url):
    '''
    获取每个主题的初始页面的入口
    :param url:
    :return:
    '''
    driver.get(url)


def get_subjects():
    subjects = driver.find_elements_by_css_selector('.image-container ')
    for sub in subjects:
        a = sub.find_elements_by_css_selector('.image-container a')[1]
        print(a)


def get_image():
    pass

def download():
    pass

if __name__ == '__main__':
    url = 'https://8xro.com/html/category/photo/page/'
    # 从第一页开始进行遍历，总页数为32页
    for i in range(1,33):
        init(url+str(i))
        get_subjects()