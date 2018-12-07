'''
python中字符串的学习（str)

在Python中字符串的定义有三种：
1.使用一对单引号来定义，如：'python'
2.使用一对双引号来定义，如："python"
3.使用一对三引号来定义，如：\'''python\'''

一般使用过程中，使用比较多的是单引号or双引号
'''

# 字符串的编码
#================================

# 在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

# 例如输出中文
print('我爱中国')

#python中使用ord()函数获取一个字符的整数表示,使用chr()函数转换为对应的字符
print(ord('中')) # 20013
print(chr(20013)) # 中

'''
由于Python的字符串类型是str，在内存中以Unicode表示，
一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。

Python对bytes类型的数据用带b前缀的单引号或双引号表示：
byte = b'我爱学习'
'''

# python中encode（） 和 decode（）的用法
#===============================================
# 将中文转换为bytes字节形式存储
data = '好好学习，天天向上'.encode('utf-8')
print(data)

#将bytes数据转换为字符形式
data = data.decode('utf-8')
print(data)

