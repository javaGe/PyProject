#coding=utf-8
'''
由于平时使用爬虫时，由于请求频繁
会导致网站封IP
所有可以自己建立一个代理池，来更换IP

IP来源网站：http://www.xicidaili.com/wn/
'''


import urllib.request
from bs4 import BeautifulSoup

#获取IP的方法，传入的参数就是要爬的页数
def getIP(pageNum):
    #ip存储的文件
    ipfile = open('ips.csv', 'w', encoding='utf-8')

    #目标url
    url = 'http://www.xicidaili.com/wn/'
    #url = "http://www.baidu.com"
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    headers = {'User-agent':user_agent}
    for i in range(1, pageNum+1): #翻页处理
        ipurl = url+str(pageNum) #拼接url
        req = urllib.request.Request(ipurl, headers=headers)
        content = urllib.request.urlopen(req).read()
        #print(content)
        bs = BeautifulSoup(content, 'lxml') #使用beautifulsoup
        trs = bs.find_all('tr')  #获取所有的tr
        for tr in trs: #遍历
            try:
                tds = tr.find_all('td')
                ipfile.write(tds[1].text+":"+tds[2].text+'\n') #写入文件
            except Exception as e:
                print(e)
    ipfile.close()

def main():
    getIP(1)

if __name__ == '__main__':
    main()