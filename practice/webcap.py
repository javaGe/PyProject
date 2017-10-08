# -*- coding: utf-8 -*-
#

from selenium import webdriver
import time
import pymysql
import os
import traceback

db = pymysql.connect("192.168.0.19", "root", "root", "icdb_dev", charset='utf8mb4')
brower = webdriver.PhantomJS()
brower.implicitly_wait(30)
brower.set_window_size(1280, 800)
SNAPSHOT_PATH = 'D:/ic_files/SNAPSHOT/20170929/'
#创建快照文件夹
if not os.path.exists(SNAPSHOT_PATH):
	os.makedirs(SNAPSHOT_PATH)

id_url = {} #存储数据库中查询的id和url

def select():
	try:
		cur = db.cursor()
		# sql = "select Article_ID, Article_URL from Article order by Program_Tag desc"
		# curDate = time.strftime('%Y-%m-%d', time.localtime())
		# sql = "select Article_ID, Article_URL from Article where Creation_Date REGEXP '^" + curDate + ".*'" + " and Program_Tag!='WechatSpider_cgc' and Snapshot_URL ='' order by Program_Tag desc"
		sql = 'select Article_ID, Raw_File_Path FROM Article where Creation_Date regexp "2017-09-29.*" and Program_Tag="toutiaoSpider_hmh"and Snapshot_URL =""'
		cur.execute(sql)
		results = cur.fetchall()
		for row in results:
			aid = row[0]
			url = row[1].replace('D:/ic_files', 'http://192.168.0.19')
			id_url[aid] = url
	except Exception as e:
		print(e)

def snapshot():
	print(id_url)
	num = 0
	try:
		for key in id_url:
			start = time.time() #开始时间
			try:
				brower.get(id_url[key])
				print (id_url[key])
				time.sleep(2)
				# 保存截图
				pic_path = SNAPSHOT_PATH + key + '.png' #快照路径
				brower.save_screenshot(pic_path)
			except Exception as e:
				error = traceback.format_exc()
				print(error)
				continue
			num += 1
			#更新数据库
			update(key, pic_path)
			print("用时：%s" %str(time.time() - start))
		print("总截图数：%s" %num)
		return num
	except Exception as e:
		print(e)


def update(id, pic_path):
	try:
		cur = db.cursor()
		sql = "update Article set Snapshot_URL='%s' where Article_ID='%s'" %(pic_path, id)
		cur.execute(sql)
		db.commit()
		print('更新快照链接成功')
	except Exception as e:
		db.rollback()
		print (e)



def main():
	select()
	num = snapshot()
	brower.close()
	return num

if __name__ == '__main__':
	main()