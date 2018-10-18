'''
元组的学习
元组也是python中的一种数据结构
元组的长度是固定的不可改变的（不可变对象）

元组一旦定义好，长度固定，元素不可更改
可以进行拼接、删除、切分、转换为list
'''

#定义一个元组 格式：tuple=(....)
tup1 = (1, 2, 3) #括号有时可以省略
print("根据下标获取元素:", tup1[1]) # 2
print("截取：", tup1[:2]) # (1, 2)

#只有一个元素是的写法：
tup2 = (1,) #需要在元素后添加一个逗号（类型为元组），不加默认括号是一个运算符（类型为整形）

#元组的拼接
tup3 = tup1 + tup2
print(tup3) #(1, 2, 3, 1)

#不能直接对某个下标值进行改变
# error >> tup3[1] = 10

#删除元组,删除后元组不存在，输出报错
del tup3
# error >> print(tup3)

'''
元组中的函数：
    长度：len(tuple)
    最大值：max(tuple)
    最小值：min(tuple)
    list转tupel: tuple(list)
'''
print("tup1的长度：", len(tup1)) # 3
print("tup1的最大值：", max(tup1)) # 3
print("tup1的最小值：", min(tup1)) # 1

ls = [1, 2] #list
t = tuple(ls) #转换
print(t) #(1, 2)

'''
遍历元组
'''
#迭代
tup4  = ('a', 'b', 'c', 'd')
it = iter(tup4)
while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        break

    #for循环 %B5%C7%C2%BC
print()
for i in tup4:
    print(i, end=" ")

print("%B5%C7%C2%BC".encode('utf-8'))

