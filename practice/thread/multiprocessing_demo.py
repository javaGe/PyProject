## 多进程学习（multiprocessing）
'''

'''
import multiprocessing
import time

'''
Process类的使用
每个进程都用一个Process类来表示
Process(group, target, name, args, kwargs)
group:表示分组，一般不用
target：表示调用对象，传入方法名字
name：进程的别名
args：调用对象所需要的参数，如，a函数有两个参数m,n 那么args需要传入（m, n）元组形式
kwargs:调用对象的字典
'''

def process(num):
    print('process',num)
if __name__ == '__main__':

    for i in range(2):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()
    print('cpu number:%s' %(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print(p.name+" "+str(p.pid))
