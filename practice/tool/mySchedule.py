import schedule
import time

def job():
    print("I'm working...")


schedule.every(2).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

'''
上面的意思就是：

每隔十分钟执行一次任务

每隔一小时执行一次任务

每天的10:30执行一次任务

每周一的这个时候执行一次任务

每周三13:15执行一次任务

run_pending：运行所有可以运行的任务


当然，如果函数中带有参数怎么办呢？

很简单，如下所示：

import schedule
import time
 
def job(name):
    print("her name is : ", name)
 
name = xiaona
schedule.every(10).minutes.do(job, name)
schedule.every().hour.do(job, name)
schedule.every().day.at("10:30").do(job, name)
schedule.every(5).to(10).days.do(job, name)
schedule.every().monday.do(job, name)
schedule.every().wednesday.at("13:15").do(job, name)
 
while True:
    schedule.run_pending()
    time.sleep(1)


'''