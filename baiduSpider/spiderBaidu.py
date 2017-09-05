import os
import re
import time
import uuid
import pymysql as db

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# 导入等待事件的包
from selenium.webdriver.support import expected_conditions as EC

from baiduSpider.config import *
from pyquery import PyQuery as pq

browser = webdriver.Chrome()
#browser = webdriver.PhantomJS()
wait = WebDriverWait(browser, 10)

# 文件保存路径
path = 'D:\\baidu\\' + time.strftime("%Y-%m-%d", time.localtime())
os.makedirs(path)

'''
使用百度进行搜索
'''
def search():
    try:

        url = 'http://www.baidu.com?tn=baiduhome'
        browser.get(url)
        # 获取输入框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#kw'))
        )
        # 输入查询关键字
        input.send_keys(KEY_WORD)

        # 获取搜索点击按钮
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#su'))
        )
        submit.click()
        searchTool = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#container > div.head_nums_cont_outer.OP_LOG > div > div.nums > div'))
        )
        # 点击搜索工具
        searchTool.click()
        choBtn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        '#container > div.head_nums_cont_outer.OP_LOG > div > div.search_tool_conter > span.search_tool_tf > i'))
        )
        choBtn.click()
        # 选择时间范围（一天）
        dateScope = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#c-tips-container > div:nth-child(1) > div > div > ul > li:nth-child(2) > a'))
        )
        dateScope.click()
        process_html(page_flag=0)
    except TimeoutException:
        return search()


'''
处理页面获取相应字段
'''
list_url = {} #用于存储所有的详情url

def process_html(page_flag):
    print('开始解析页面')
    try:
        # 判断内容是否全部加载完成
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#content_left'))
        )
        # 获取页面源代码
        html = browser.page_source
        # 转换成bs对象
        bs = BeautifulSoup(html, "lxml")
        result_div = bs.find(id='content_left')  # 获取需要的内容

        for i in range(10):
            data_index = str(page_flag + i + 1)
            data_div = result_div.find(id=data_index)  # 每个标题的div

            title = data_div.find('h3')
            str_title = title.a.get_text().strip()  # 文章标题
            str_url = title.a['href'].strip()  # 文章url

            str_source = "来源未知"  # 原始网站来源
            source_site = data_div.find(class_="c-showurl")
            if not source_site is None:
                site = source_site.get_text()
                if '//' in site:
                    str_source = site.split('/')[2].strip()
                else:
                    str_source = site.split('/')[0].strip()
            abstract = ""  # 文章的摘要
            abs = data_div.find(class_="c-abstract")
            if not abs is None:
                abstract = abs.get_text().strip()
            photo_url = ''  # 图片的来源
            photo = data_div.find('img')
            if not photo is None:
                photo_url = photo.get('src')
            print(str_title, '>>>>>', str_source, '>>>>', str_url, '>>>>', abstract, '>>>>', photo_url)

            artcle_id = str(uuid.uuid1())
            result = {
                'title': str_title,  # 标题
                'abstract': abstract,  # 摘要
                'photo_url': photo_url,  # 图片url
                'source_site': str_source,  # 来源网站
                'article_url': str_url,  # 文章url
                'article_id': artcle_id,  # 文章id
                'category_id': '',
                'publish_time': time.strftime('%Y-%m-%d', time.localtime()),
                'media_type': 1,  # 文章类型（html）
            }
            # 获取标题页面
            # get_html(str_url, artcle_id)
            list_url[artcle_id] = str_url
            # 数据入库
            save_mysql(result)
    except TimeoutException:
        return process_html()


# 获取页面 html,下载到本地    http://newpaper.dahe.cn/hnrb/html/2017-09/01/content_181007.htm
def get_html(dict):
    print('获取页面html')
    # driver = webdriver.Chrome()
    for key in dict:
        browser.get(dict[key]) #请求每个详情url
        time.sleep(5) #等待5秒
        print('文章链接》》》》',dict[key])
        html = browser.page_source
        str = re.sub(r'([Cc]harset=*)(.*?")', r'\1utf-8"', html)
        try:
            f = open(path+"\\"+key+".html", 'w', encoding='utf-8')
            f.write(str)
        except Exception:
            print("写入失败")
        finally:
            f.close()


# 数据入库
def save_mysql(dict):
    # 连接数据库
    conn = db.connect(
        host=DB_URL,
        port=DB_PORT,
        user=DB_USER,
        passwd=DB_PASSWD,
        database=DB,
        charset=DB_CHARSET
    )
    # 获取游标
    cur = conn.cursor()

    # 插入时间
    curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 当前日期
    curDate = time.strftime('%Y-%m-%d', time.localtime())
    # 文件路径
    file_path = path + "\\" + dict['article_id'] + ".html"
    article_id = dict['article_id']  # 文章id
    title = dict['title']  # 标题
    abstract = dict['abstract']  # 摘要
    photo_url = dict['photo_url']  # 图片url
    media_type = dict['media_type']  # 文章类型
    source_site = dict['source_site']  # 来源网站
    article_url = dict['article_url']  # 文章url
    lis = (
    article_id, title, '', curDate, abstract, photo_url, media_type, file_path, '', source_site, article_url, KEY_WORD,
    '', curTime, curTime, 1)
    print(lis)

    sql = '''INSERT INTO article VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    try:
        # 插入数据
        cur.execute(sql, lis)
        conn.commit()
        print("数据插入成功")
    except Exception as e:
        conn.rollback()
        print('插入数据失败')
        print(e)
    finally:
        conn.close()


'''
处理分页
'''
def next_page(pageNum, page_flag):
    try:
        # 判斷點擊按鈕是否可用
        submit = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, '下一页>'))
        )
        submit.click()
        # 判斷當前頁是否是和頁碼相同
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page > strong > span.pc"), str(pageNum))
        )

        # 獲取頁面信息
        process_html(page_flag)
    except Exception as e:
        print(e)
        #return next_page(pageNum, page_flag)


# 程序入口
def main():
    try:
        search()
        page_flag = 10
        for i in range(2, 51):
            time.sleep(3)
            next_page(i, page_flag)
            page_flag += 10
            print('第 %d 页' % i)
        #获取页面html
        get_html(list_url)
    except Exception as e:
        print('出错了')
        print(e)
    finally:
        browser.quit()



'''

'''
if __name__ == '__main__':
    main()