# coding=utf-8
import os
import pymysql

def update(id, url):
    try:

        db = pymysql.connect('192.168.0.19', 'root', 'root', 'icdb_dev', charset='utf8mb4')
        cur = db.cursor()
        sql = "update Article set Snapshot_URL='%s' where Article_ID='%s' and Snapshot_URL=''" % (url, id)
        cur.execute(sql)
        db.commit()
        print('更新快照链接成功')
    except Exception as e:
        db.rollback()
        print("更新失败"+e)

path = "D:/ic_files/SNAPSHOT"
lis = os.listdir(path)
for dir in lis:
    files = os.listdir(path+'/'+dir)
    for file in files:
        id = file.replace('.png', '')
        url = path+"/"+dir+"/"+file
        # print(id+">>>>>"+url)
        update(id, url)
    # print(files)
# print(lis)
