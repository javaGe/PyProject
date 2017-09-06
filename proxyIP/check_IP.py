#coding=utf-8
'''
校验提取的id是否都有效
校验方法：
使用这些代理IP去请求百度
两秒内能请求成功，证明可用
'''
import socket
import csv
import urllib.request

def check():
    socket.setdefaulttimeout(2) #定义默认时间2秒
    #读取文件
    read = open('ips.csv', 'r')
    lines = read.readlines()
    #有效IP存储
    valid_ip = open('valid_ip.csv', 'w', encoding='utf-8')
    print(lines)
    num = 0
    for row in lines:
        print(row)
        proxy_handler = urllib.request.ProxyHandler({'http':row}) #设置代理
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener) #注册
        try:
            #请求网页
            urllib.request.urlopen('http://www.baidu.com')
            print('有效IP：',row)
            num += 1
            #将有效的IP存入文件
            valid_ip.write(row+'\n')
        except Exception as e:
            print(e)
            continue
    print('有效IP个数：',num)
    valid_ip.close()


def main():
    check()


if __name__ == '__main__':
    main()