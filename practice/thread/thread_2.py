#coding=utf-8
import threading
import time
'''
使用threading模块
将某个类需要多线程执行的，创建时继承threading.Thread
将线程进行同步
threadlock = threading.Lock():线程锁
获取锁：threadlock.acquire()
释放锁：threadlock.realese()

'''


class myThread(threading.Thread):
    '''
    自定义线程类，继承父类threading.Thread
    '''
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID #线程id
        self.name = name #线程名称
        self.counter = counter #计数
    def run(self): #run执行需要执行的代码
        print('starting'+self.name)

        #获取锁
        threadlock.acquire() #可以设置获取锁的超时时间timeout，超时返回false

        print_time(self.name, self.counter, 5)

        #释放锁
        threadlock.release()

        print('end'+self.name)

#线程执行的函数
def print_time(threadname, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s, %s' %(threadname, time.ctime(time.time())))#time.ctime(time.time()))将当地时间转换为字符串
        counter -= 1

#创建一个锁
threadlock = threading.Lock()
#线程列表
threads = []

#创建线程
thread1 = myThread(1, 'thread_1', 1)
thread2 = myThread(2, 'thread_2', 2)

#开启线程
thread1.start()
thread2.start()

#将线程添加到列表中
threads.append(thread1)
threads.append(thread2)

#遍历，等待线程执行完毕
for t in threads:
    t.join()

print("exit mian thread")



