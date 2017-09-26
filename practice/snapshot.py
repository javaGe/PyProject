# coding=utf-8
import pymysql
from selenium import webdriver
import time
import os


browser = webdriver.PhantomJS()
browser.set_window_size(1200, 900)
browser.implicitly_wait(30)


def html2pic(url, pic_name):
    '''
    将网页转成图片
    :param url: 页面url
    :param name:  图片名称
    :return:
    '''
    try:
        browser.get(url)  # Load page
        time.sleep(2)
        # 页面过长时，往下轮动
        browser.execute_script("""
               (function () {
                   var y = 0;
                   var step = 100;
                   window.scroll(0, 0);

                   function f() {
                       if (y < document.body.scrollHeight) {
                           y += step;
                           window.scroll(0, y);
                           setTimeout(f, 100);
                       } else {
                           window.scroll(0, 0);
                           document.title += "scroll-done";
                       }
                   }

                   setTimeout(f, 1000);
               })
           """)

        for i in range(30):
            if "scroll-done" in browser.title:
                break
            time.sleep(3)

        # 保存截图
        browser.save_screenshot("D:\\snapshot\\" + pic_name)
    except Exception as e:
        print(e)
        return html2pic(url, pic_name)


id_url = {}


def select():
    try:
        db = pymysql.connect("192.168.0.19", "root", "paladata", "ICDB_Dev")
        cur = db.cursor()
        sql = 'SELECT Article_ID, Article_URL FROM Article WHERE Program_Tag in("BaiduSpider_GGF","toutiaoSpider_hmh")'
        cur.execute(sql)
        result = cur.fetchall()
        for raw in result:
            id = raw[0]
            article_url = raw[1]
            id_url[id] = article_url
    except Exception as e:
        print(e)
    finally:
        db.close()

def main():
    select()
    print(id_url)
    num =  0
    # for key in id_url:
    #     html2pic(id_url[key], key + '.png')
    #     print("第%s张" % num)
    #     num += 1
    # browser.quit()

    # d = {#'1': 'http://blog.csdn.net/marksinoberg/article/details/58644436',
    #      # '2': 'http://www.jb51.net/article/52329.htm',
    #      '4': 'http://data.eastmoney.com/notices/detail/002903/AN201709250910088062,JUU1JUFFJTg3JUU3JThFJUFGJUU2JTk1JUIwJUU2JThFJUE3.html'}

    for key in id_url:
        args1 = id_url[key]
        args2 = key
        start = time.time()
        os.system('phantomjs js_snapshot.js {0} {1}'.format(args1, args2))
        end = time.time()
        print("用时：%s" %str((end - start)))
        print("第%s张" % num)
        num += 1

if __name__ == '__main__':
    main()