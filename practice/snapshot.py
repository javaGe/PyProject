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
        #sql = 'SELECT Article_ID, Article_URL FROM Article WHERE Creation_Date REGEXP "2017-09-27.*" and Program_Tag = "BaiduSpider_GGF"'
        sql = 'SELECT Article_ID, Raw_File_Path FROM Article where Creation_Date REGEXP "2017-09-27.*" and Program_Tag in ("WechatSpider_cgc","toutiaoSpider_hmh")'
        #sql = 'SELECT Article_ID, Raw_File_Path FROM Article where Creation_Date REGEXP "2017-09-11.*" and Program_Tag="toutiaoSpider_hmh"'
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
    print(id_url.__len__())
    num = 1
    path = 'D:/SNAPSHOT/20170927/'
    if not os.path.exists(path):
        os.makedirs(path)
    action = time.time()
    for key in id_url:
        args1 = id_url[key].replace('D:/ic_files', 'http://192.168.0.19')
        #args1 = id_url[key]
        args2 = path + key+'.png'
        start = time.time()
        os.system('phantomjs js_snapshot.js {0} {1}'.format(args1, args2))
        end = time.time()
        print("用时：%s" % str((end - start)))
        print("第%s张" % num)
        num += 1
    print('总用时长：%s' % str((time.time() - action)))

if __name__ == '__main__':
    main()