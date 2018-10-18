# age = True
# if age:
#     print("你好！")
# else:
#     print("hello world!")

n = 123
f = 456.789
s1 = 'hello world'
s2 = 'hello,\'adam\''
s3 = r'''hello,
lisa!'''

print(s3)
print(n, f)
#=================================================================
#python 字符串的学习
#函数ord():获取字符的整数表示ord（‘a’）>65
#函数chr():把编码转换为对应的字符chr('中')>20013



#python中的byte类型表示：x = b'abc'>>表示的是byte类型的

#str类型转换为byte类型
#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
#‘abc’.encode('ascii'):转换为ascii编码
#‘中文’.encode('utf-8'):转换为utf-8编码

#当从网络中获取的内容可以使用decode解码为某种编码：b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'):中文

#计算长度的函数len()
#字母占一个字节，中文占三个字节
a = len("akljdklajfl")
print("字符的长度为：", a)

b = len(b'abcdc')
print("byte类型的长度：",b)

# s1 = int(input("请输入小明去年的成绩："))#类型转换
# s2 = int(input("输入小明今年的成绩："))
# print("成绩计算中。。。。")
# p = (s2 -s1) / s1 *100
# print("小明成绩提高的百分比为：%.1f%%" %p)

#python中的集合list和tuple
#================================================
#list是可变的集合
#方法：append():添加方法
#pop()删除的方法
l = [
    ['abc','bcd','efg'],
    ['dkdk','kdkd','kdfd'],
    ['ksklj','kdsfl']
]

print("l的元素个数：",len(l))

#python中的判断语句
#============================================

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 80.5

bmi = weight / (height * height)
if bmi < 18.5:
    print("过轻")
elif bmi>18.5 and bmi<25:
    print("正常")
elif bmi>25 and bmi<28:
    print("过重")
elif bmi>28 and bmi<32:
    print("肥胖")
else:
    print("严重肥胖")

#=========================================================
#python中for循环学习
#结构：for x in xxx
#range()函数：生成一个有序的整数序列
#如：range(10):0~9>>>转换成list：list(range(10))

# array = list(range(10))
# for a in array:
#     print(a)

# while 1:
#     print("hh")

# for a in "aldflkjks":
#     print(a)

#python中的dict和set
#==================================================
# dic = {'1':"libai", '2':"zhangfei", '3':"guanyu"}
# print(dic['1'])
# print(dic)


#函数的使用
#==========================================
#将十进制数转换为十六进制数

h = hex
n1 = 255
n2 = 1000
print(h(n1))
print(h(n2))


#函数的定义，使用def关键字
def _demo_(str):
    if '1'.__eq__(str):
        print(1)
    elif '0'.__eq__(str):
        print(0)


_demo_("1")

#迭代器的使用
list = [1, 2, 3, 4, 5]
it = iter(list)
# for i in it:
#     print(i, end=" ")
i = list.__len__()
print("i的长度%d" %i)
while i > 0:
    i -= 1
    #print(next(it), end=" ")

a, b, c = 1, 2, 3

print(a, b, c, end=" ")

s = 'Python was started in 1989 by \'Guido\'\nPython is free and easy to learn.'
print (s)
print(r"""'\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'""")
s = "'\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'"
print(str(s))

for i in range(1,10):
    for j in range(0,10):
        if i < j:
            print(i*10+j, end=" ")


#========================================
print()
d = {1:"a", 2:"b", 3:"c"}
d[4] = "d"
d[1] = "f"
print(d)

