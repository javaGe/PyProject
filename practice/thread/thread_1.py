#coding=utf-8
'''
对多线程的练习
多线程创建的方式
1.导入_thread模块
2.定义线程启动的函数
3.调用start_new_thread('启动的函数'， （‘函数参数’）)
'''

import _thread
import time

#给线程定义一个函数
def print_time(threadname, delay):
    count = 0
    while count < 5:
        count += 1
        print('threadname %s, curtime %s' %(threadname, time.ctime(time.time())))

#创建两个线程
try:
    _thread.start_new_thread(print_time, ('thread_1', 2))
    _thread.start_new_thread(print_time, ('thread_2', 4))
except:
    print('Error:unable to start thread')

time.sleep(5)

print('thread end')
