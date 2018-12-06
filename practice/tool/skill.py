# coding=utf-8

'''
python编程中的小技巧

'''

# ==========遍历一个序列===============

# colors = ['red','green','blue','yellow']
# # 平常用法,遍历下标进行打印
# for i in range(len(colors)):
#     print(colors[i])

# 优化用法，直接进行遍历，因为序列可以直接进行迭代
# for color in colors:
#     print(color)


#============倒序遍历================
colors = ['red','green','blue','yellow']
# 用range的负数来遍历 ,range(num, step, stop)
for i in range(len(colors)-1, -1, -1):
    print(colors[i])

# 优化方法，使用反转直接倒序输出
for color in reversed(colors):
    print(color)


#===========遍历两个序列=============
names = ['leo','lili','ggf']
colors = ['red','green','blue','black']

# Bad
n = min(len(names), len(colors))
for i in range(n):
    print(names[i],'-->',colors[i])

# Batter
for name, color in zip(names, colors):
    print(name, '-->', color)


#============遍历排序的序列===================
colors = ['red','green','blue','yellow']
# 正序遍历
for color in sorted(colors):
    print(color)

# 倒序遍历
for color in sorted(colors, reverse=True):
    print(color)


# ==========自定义排序=================
colors = ['red','green','blue','yellow']
#Bad
def compare_length(c1, c2):
    if len(c1) > len(c2): return -1
    if len(c1) < len(c2): return 1
    return 0
#print(sorted(colors, cmp=compare_length))

#Better
print(sorted(colors, key=len))

#==========遍历文件遇到指定字符后退出===========
#bad
# blocks=[]
# # while True:
# #     block = f.read[32]
# #     if block == '':
# #         break
# #
# #     blocks.append(block)

#better
#  iter是一个内置函数用来生产迭代器，partial的不断的读入文件中32字节，
# 注意iter引入第二个参数，表示当读入的内容是''的时候，会触发生成器stop！
# blocks=[]
# # if block in iter(partial(read,32),''):
# #     bolcks.append(block)