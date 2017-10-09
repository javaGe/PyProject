## 线程的优先队列（queue）
'''
queue模块提供同步的，线程安全的队列

queue模块中的常用方法：
    Queue.qsize():返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]])获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''

import queue
import threading
import time

exitFlag = 0

# 创建线程
class myThread(threading.Thread):
    def __init__(self, threadid, name, q):
        threading.Thread.__init__(self)
        self.threadid = threadid
        self.name = name
        self.q = q

    def run(self):
        print('start' + self.name)
        process_data(self.name, self.q)
        print('end' + self.name)

#处理队列中的数据
def process_data(threadname, q):
    while not exitFlag:
        if not workQueue.empty():  # 判断队列不为空时，执行
            data = q.get()  # 获取多队列内容
            print('%s process %s' % (threadname, data))
        time.sleep(1)


threadList = ['thread_1', 'thread_2', 'thread_3']  # 线程名称列表
nameList = ['one', 'two', 'three', 'four', 'five']  # 队列数据名称列表
# queueLock = queue.Lock()  # 队列锁
workQueue = queue.Queue(10)  # 设置队列大小
threads = []  # 启动后线程列表
threadID = 1  # 线程id

# 创建线程
for tname in threadList:
    t = myThread(threadID, tname, workQueue)
    t.start()
    threads.append(t)
    threadID += 1

# 填充队列，往队列中添加数据
for work in nameList:
    workQueue.put(work)

# 等待队列数据清空
while not workQueue.empty():
    pass

# 通知线程退出
exitFlag = 1

# 等待所有线程退出
for t in threads:
    t.join()

# 退出主程序
print('exit main thread')


