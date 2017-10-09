import socket

'''
客户端
实现发送信息到服务端
'''

sk = socket.socket() #创建socket对象
sk.connect(('127.0.0.1', 10001)) #初始化与服务端的连接
while True:
    send_data = input('输入内容：')
    sk.sendall(bytes(send_data, encoding='utf-8')) #发送信息（byte类型的数据），utf-8编码
    if send_data == 'byebye':
        break
    accept_data = str(sk.recv(1024), encoding='utf-8')
    print('接收内容：',accept_data)
sk.close()