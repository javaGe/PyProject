# coding=utf-8
'''
python对MongoDB的增删改查的操作
'''
from pymongo import MongoClient

# 连接mongo
client = MongoClient('localhost', 27017)
# 连接数据库
db = client.pythondb
# 获取数据库中的集合
coll = db.qiushi

'''
添加数据

insert 和 save 的使用
insert可以插入一个列表
save对于列表需要进行遍历
'''
# stus = [{'name':'ggf', 'age':22, 'gender':'man'},
#        {'name':'ddd', 'age':22, 'gender':'woman'},
#        {'name': 'ddd', 'age': 22, 'gender': 'woman'},
#        {'name': 'ddd', 'age': 22, 'gender': 'woman'},
#        {'name': 'ddd', 'age': 22, 'gender': 'woman'},
#        {'name': 'ddd', 'age': 22, 'gender': 'woman'}]
# # coll.insert(stu) # 添加一个列表
# for stu in stus:
#     coll.save(stu) # 添加一个字典

'''
更新数据
'''
# coll.update_one({'name':'ddd'},{'$set':{'name':'abc'}}) # 修改一个
# coll.update_many({'name':'ddd'}, {'$set':{'name':'aaa'}}) # 修改所有
# coll.replace_one({"name":'aaa'}, {'name':'ccc'})
'''
查询数据
'''
# result = coll.find({'name':'aaa'})
# print(result)
# 查询年龄大于20，第二个{}表示哪个显示哪个不显示，1：显示，0：不显示
for result in coll.find({'age':{'$gt':20}}, {'name':1, 'age':1, '_id':0}):
    print(result)
# result = coll.find({'name':'ggf'}, projection=['name', 'age'])
# for key in result:
#     print(result[key])
# print(result)

'''
#1.查询身高小于180的文档
print '-------------身高小于180:'
print type(collection_set01.find({'high':{'$lt':180}})) #<class 'pymongo.cursor.Cursor'>
for r in collection_set01.find({'high':{'$lt':180}}):
    print r
print type(collection_set01.find_one({'high':{'$lt':180}})) #<type 'dict'>
print 'use find_one:',collection_set01.find_one({'high':{'$lt':180}})['high']
print 'use find_one:',collection_set01.find_one({'high':{'$lt':180}})

#2.查询特定键(select key1,key2 from table;)
print '-------------查询特定键--------'
print '-------------查询身高大于170,并只列出_id,high和age字段(使用列表形式_id默认打印出来,可以使用{}忽视_id):'
for r in collection_set01.find({'high':{'$gt':170}},projection=['high','age']):print r
print '\n'
print '--------------skip参数用法'
for r in collection_set01.find({'high':{'$gt':170}},['high','age'],skip=1):print r #skip=1跳过第一个匹配到的文档
for r in collection_set01.find({'high':{'$gt':170}},['high','age']).skip(1):print r #skip=1跳过第一个匹配到的文档
print '\n'
print '--------------limit参数用法'
for r in collection_set01.find({'high':{'$gt':170}},['high','age'],limit=1):print r #limit=2限制显示2条文档
print '\n'
print '--------------用{}描述特定键'
for r in collection_set01.find({'high':{'$gt':170}},{'high':1,'age':1,'_id':False}):print r

print '---------------------多条件查询'
print collection_set01.find_one({'high':{'$gt':10},'age':{'$lt':26,'$gt':10}})

#3.$in
print '----------------IN'
for r in collection_set01.find({"age":{"$in":[23, 26, 32]}}): print r  # select * from users where age in (23, 26, 32)
#for u in db.users.find({"age":{"$nin":(23, 26, 32)}}): print u # select * from users where age not in (23, 26, 32)

#4.count统计数目
print '----------------count'
print collection_set01.find({"age":{"$gt":20}}).count() # select count(*) from set01 where age > 10

#5.$or
print '----------------条件或'
print '大于等于29或者小于23'
for r in collection_set01.find({"$or":[{"age":{"$lte":23}}, {"age":{"$gte":29}}]}): print r

#6.$exists，是否存在字段
print '------------exists'
for r in collection_set01.find({'age':{'$exists':True}}):print 'age exists',r # select * from 集合名 where exists 键1
for r in collection_set01.find({'age':{'$exists':False}}):print 'age not exists',r # select * from 集合名 where not exists 键1

#7.正则表达式查询
print '正则表达式查询'
#method 1
for r in collection_set01.find({'name':{'$regex':r'.*wei.*'}}):print r   #找出name字段中包含wei的文档
#method 2
import re
Regex = re.compile(r'.*zhang.*',re.IGNORECASE)
for r in collection_set01.find({'name':Regex}):print r   #找出name字段中包含wei的文档


#8.sort排序

print '--------------------使用sort排序(文档中没有排序的字段也会打印出来,表示最小)'
#pymongo.ASCENDING      1
#pymongo.DESCENDING     -1
#sort([[],()]),[],()均可
print '--------------age 升序'
for r in collection_set01.find().sort([["age",pymongo.ASCENDING]]):print r
print '--------------age 降序'
for r in collection_set01.find().sort([("age",-1)]):print r
print '--------------age升序,high升序'
for r in collection_set01.find().sort((("age",pymongo.ASCENDING),("high",pymongo.ASCENDING))):print r
print '--------------age升序，high降序'
for r in collection_set01.find(sort=[("age",pymongo.ASCENDING),("high",pymongo.ASCENDING)]):print r


#9.$all判断数组属性是否包含全部条件,注意与$in区别

print '-------------$all'
for r in collection_set01.find({'list':{'$all':[2,3,4]}}):print r
print '-------------$in'
for r in collection_set01.find({'list':{'$in':[2,3,4]}}):print r


#10.$size匹配数组属性元素数量
print '-------------$size'
print '-------------size=3'
for r in collection_set01.find({'list':{'$size':3}}):print r
print '-------------size=7'
for r in collection_set01.find({'list':{'$size':7}}):print r

#11.$unset和$set相反表示移除文档属性
print '-------------------$unset'
print '---before'
for r in collection_set01.find({'name':'weijian'}):print r
collection_set01.update({'name':'weijian'},{'$unset':{'age':1}})
print '---after'
for r in collection_set01.find({'name':'weijian'}):print r
'''

'''
删除数据
'''
coll.delete_one({'name':'ggf'}) # 删除一个符合的集合
coll.delete_many({'name':'aaa'}) # 删除多个
coll.delete_many({}) # 删除所有

print(coll.count())



