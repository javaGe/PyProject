'''
用法参考
https://lz5z.com/Python%E5%AE%9A%E6%97%B6%E4%BB%BB%E5%8A%A1%E7%9A%84%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F/

date
最基本的一种调度，作业只会执行一次。它的参数如下：

run_date (datetime|str) – the date/time to run the job at
timezone (datetime.tzinfo|str) – time zone for run_date if it doesn’t have one already


from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
def my_job(text):
    print(text)
# The job will be executed on November 6th, 2009
sched.add_job(my_job, 'date', run_date=date(2009, 11, 6), args=['text'])
sched.add_job(my_job, 'date', run_date=datetime(2009, 11, 6, 16, 30, 5), args=['text'])
sched.add_job(my_job, 'date', run_date='2009-11-06 16:30:05', args=['text'])
# The 'date' trigger and datetime.now() as run_date are implicit
sched.add_job(my_job, args=['text'])
sched.start()

cron

year (int|str) – 4-digit year
month (int|str) – month (1-12)
day (int|str) – day of the (1-31)
week (int|str) – ISO week (1-53)
day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
hour (int|str) – hour (0-23)
minute (int|str) – minute (0-59)
second (int|str) – second (0-59)
start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)


from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print("Hello World")
# BlockingScheduler
sched = BlockingScheduler()

# Schedules job_function to be run on the third Friday
# of June, July, August, November and December at 00:00, 01:00, 02:00 and 03:00
sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

# Runs from Monday to Friday at 5:30 (am) until 2014-05-30 00:00:00
sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2014-05-30')
sched.start()


interval
参数：

weeks (int) – number of weeks to wait
days (int) – number of days to wait
hours (int) – number of hours to wait
minutes (int) – number of minutes to wait
seconds (int) – number of seconds to wait
start_date (datetime|str) – starting point for the interval calculation
end_date (datetime|str) – latest possible date/time to trigger on
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print("Hello World")
# BlockingScheduler
sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', hours=2)
# The same as before, but starts on 2010-10-10 at 9:30 and stops on 2014-06-15 at 11:00
sched.add_job(job_function, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')
sched.start()
'''

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
# 周一到周五 6:30 启动
scheduler.add_job(job, 'cron', day_of_week='sat', hour=20, minute=20)
# 每间隔一分钟调度一次
# scheduler.add_job(job, 'interval', minutes=1)
# 每间隔一秒调度一次
# scheduler.add_job(job, 'interval', seconds=1)
scheduler.start()