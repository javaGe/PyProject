'''
linux上运行时需要设置

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8') # 设置默认编码格式为'utf-8'


1.拿到团队工作台的url：http://58.62.207.51:9990/secure/resourceManagerAction!mainpage.jspa
2.登录个人jira系统
3.进行截图，保存图片，后续将保存好的图片发送到微信群
4.编写发送群信息的函数
5.编写定时器，每天6点前发送消息：设置5:30  时间到后，执行1-4步骤

linux 部署问题:

linux中安装python库的问题：
yum install -y  epel-release #先安装epel源
yum install -y python-pip  # 接着安装pip
pip install --upgrade pip  # 更新pip到最高版本

解决linux使用phantomjs截图中文乱码问题
解决办法就是安装字体。
在centos中执行：yum install bitmap-fonts bitmap-fonts-cjk
在ubuntu中执行：sudo apt-get install xfonts-wqy

phantomjs安装问题：

1.下载安装包：
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
2.加压缩：
tar -xjvf phantomjs-1.9.7-linux-x86_64.tar.bz2

3.建立软链接：
mv /phantomjs-2.1.1-liunx-x86_64.tar.bz2 /phantomjs  重命名
ln -s /usr/local/phantomjs/bin/phantomjs /usr/bin/

4.安装依赖软件：
yum -y install fontconfig

wxpy在linux显示二维码问题：
先安装pillow库，然后设置Bot中的参数
:param console_qr:
            * 在终端中显示登陆二维码，需要安装 pillow 模块 (`pip3 install pillow`)。
            * 可为整数(int)，表示二维码单元格的宽度，通常为 2 (当被设为 `True` 时，也将在内部当作 2)。
            * 也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
'''

from selenium import webdriver as wb
# import schedule
import time
# import itchat
from wxpy import *
from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime
import requests

# 登录客户端
bot = Bot(cache_path=True)
# itchat.auto_login()
# itchat.run()

# 获取金山词霸每日一句，英文和翻译
def get_news():
    try:
        url = "http://open.iciba.com/dsapi"
        r = requests.get(url)
        contents = r.json()['content']
        translation = r.json()['translation']
        return contents, translation
    except Exception as e:
        return '采集鸡汤的程序挂啦！今天没有鸡汤，但还是要报工哟.^-^.'

def screenshots():
    '''
    获取jira上团队工作日志信息，保存为图片，获取失败返回失败信息
    :return:
    '''

    try:
        url = 'http://58.62.207.51:9990/secure/deskDomainAction!mainpage.jspa'
        # drive = wb.Chrome()
        driver = wb.PhantomJS()
        driver.implicitly_wait(30)
        driver.get(url)
        print('进入登录页面')

        user_name = driver.find_element_by_id('login-form-username')
        user_name.clear()
        user_name.send_keys('xxxxx')

        pwd = driver.find_element_by_id('login-form-password')
        pwd.clear()
        pwd.send_keys('xxxxx')

        submit = driver.find_element_by_id('login-form-submit')
        submit.click()
        print('登录成功')
        # 获取当前句柄
        current_handle = driver.current_window_handle
        # print(current_handle)

        # 登录后，进入工作日志界面
        driver.find_element_by_link_text('工作日志').click()

        # 获取所有的句柄
        handles = driver.window_handles
        # print(handles)

        # 进入第二个句柄
        driver.switch_to_window(handles[1])

        # 保存截图
        driver.get_screenshot_as_file('./test.png')

        print('截图成功！')
        time.sleep(2)
        driver.quit()
        return None
    except Exception as e:
        print('获取工作日志图片失败！')
        driver.quit()
        return '截图程序挂啦！今天没图看了，但还是要准时报工哟！！'

def sendMsg(data):
    # 获取需要发送信息的群
    group = bot.groups().search(u'test')[0]

    group.send(u'@报工一刻@') # 发送固定信息
    group.send(data)  # 发送鸡汤
    try:
        group.send_image('./test.png')  # 发送图片
    except:
        group.send(u'截图程序挂啦！今天没图看了，但还是要准时报工哟！！')

    group.send(u'没报工的赶紧了喂!0..0!')

def job():
    '''
    定时器执行的函数
    :return:
    '''

    # 获取每日news
    news = get_news()

    # # 获取截图
    # msg = screenshots()

    # 发送信息
    sendMsg(news[0]+'\n'+news[1])


# 定时执行
# schedule.every(1).minutes.do(job)

# 运行所有可运行的任务，一直运行
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# 创建调度器，周一到周五，每天17:50 发送报工信息
scheduler = BlockingScheduler()
# scheduler.add_job(job, 'cron', day_of_week='1-5', hour=17, minute=50)
scheduler.add_job(job, 'interval', seconds=30)
scheduler.start()

bot.join() #保证上述代码持续运行