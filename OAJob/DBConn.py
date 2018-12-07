import pymysql
from Pyproject.OAJob.config import *

def getDbConn():
    try:
        # 获取数据库连接
        conn = pymysql.Connect(DB_URL, DB_USER, DB_PASSWD, DB_PORT, DB_CHARSET)
        return conn
    except Exception as e:
        print('连接数据库出错！')
        print(e)

def add(conn, data):
    '''
    数据入库
    :return:
    '''

    try:
        cursor = conn.cursor()
        sql = 'insert into oajob values (%s,%s)' %(data[0], data[1])

        # 执行SQL
        cursor.execute(sql)

        # 提交到数据库
        conn.commit()
    except Exception as e:
        print('数据入库失败！！')
        print(e)

def close(conn):
    '''
    关闭数据连接
    :param conn:
    :return:
    '''
    conn.close()