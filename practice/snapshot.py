#coding=utf-8
import pymysql
from selenium import webdriver
import time

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

        #保存截图
        browser.save_screenshot(pic_name)
    except Exception as e:
        print(e)
        return html2pic(url, pic_name)

id_url = {}
def select():
    try:
        db = pymysql.connect("localhost", "root", "root", "spider")
        cur = db.cursor()
        sql = 'SELECT Article_ID, Article_URL FROM icdb_dve'
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
    for key in id_url:
        html2pic(id_url[key], key+'.png')

    browser.quit()

if __name__ == '__main__':
    main()