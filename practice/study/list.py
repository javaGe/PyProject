"""
列表的学习
对列表的增、删、改、查
列表的特性：
长度是可变的（可变对象），可以在随意位置插入元素
列表的函数，方法学习
"""


'''
list中的方法：
    添加：appeend(obj)
    插入：insert(index, obj)
    计数：count(obj)
    删除：pop(obj=list[-1])
    移除：remove(obj)
    排序：sort()
    复制：copy()
    清空：clear()
    反转：reverse()
    获取下标：index(obj)
    末尾追加其他列表：extend(list)
'''
#创建一个列表：格式list[....]
list1 = [1, 2, 3, 4, 5]

#添加元素:append()
list1.append(6)
print("末尾添加了一个元素：6>>",list1) #[1, 2, 3, 4, 5, 6]

#插入元素:insert(),这时列表中的长度会增加
list1.insert(0, "a")
print("在下标为0的位置插入：a>>", list1) #['a', 1, 2, 3, 4, 5, 6]
print()

#删除列表中的元素
del list1[0]
print("删除第一个元素：",list1) #[1, 2, 3, 4, 5, 6]

#追加列表
list2 = ['a', 'b', 'c']
list1.extend(list2)
print(list1) #[1, 2, 3, 4, 5, 6, 'a', 'b', 'c']


"""
list中的函数：
    元素个数：len(list)
    最大值：max(list)
    最小值：min(list)
    元组转列表：list(tuple)
"""
#元组转换成列表：
tp = (1, 2, 3, 4)
print('元组：', tp)    #(1, 2, 3, 4)
ls = list(tp)
print("列表：", ls)    #[1, 2, 3, 4]


"""
对列表进行截取和拼接
截取常用：list[:] 获取所有
         list[1:] 从第二个元素开始
         list[2:3] 截取下标为2的元素，不包括下标为3的
         list[::2] 间隔取值
         
拼接：即是将两个列表进行拼接形成一个list
"""

l1 = [1, 2, 3]
l2 = [4, 5, 6]
#进行拼接
l1 = l1 + l2
print(l1) #[1, 2, 3, 4, 5, 6]

print("输出前两个元素：", l1[:2])   #[1, 2]
print("输出每两间隔的第一个值：", l1[::2])  #[1, 3, 5]
print("从末尾开始取值(倒数第二个)：", l1 [-2]) # 5

'''
列表的遍历：
    for循环
    迭代
'''
#使用迭代
list3 = [1, 2, 3, 4]
it = iter(list3)
print("输出下一个：", next(it)) #1
for i in it:
    print(i, end=" ") #2 3 4

print()
#for循环遍历
for i in list3:
    print(i, end=" ")

print()
list4 = [1, 2, ['a', 'b'], 3]
for i in list4:
    print(i, end=" ")