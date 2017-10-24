from scrapy_dingdian import settings
import pymysql
import traceback
host = settings.MYSQL_HOST
user = settings.MYSQL_USER
pwd = settings.MYSQL_PASSWORD
port = settings.MYSQL_PORT
db = settings.MYSQL_DB

try:
    conn = pymysql.connect(host, user, pwd, db, charset='utf8')
    cur = conn.cursor()
except Exception as e:
    print(e)

def save(lis):
    try:

        sql = 'insert into tb_story values(%s,%s,%s,%s,%s,%s,%s)'
        cur.execute(sql, lis)
        conn.commit()
        print('存储成功')
    except Exception as e:
        ex_str = traceback.format_exc()
        conn.rollback()
        print(ex_str)