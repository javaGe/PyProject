import socket

'''
服务端，接收客户端数据
'''

sk = socket.socket()
sk.bind(('127.0.0.1', 10001))
sk.listen(5) #设置监听
while True:
    conn, addr = sk.accept() #阻塞的状态，被动的等待客户端的连接
    while True:
        accept_data = str(conn.recv(1024), encoding='utf-8')
        print('接收内容',accept_data)
        if accept_data == 'byebye':
            break
        # send_data = input('发送内容：')
        if accept_data == '1':
            with open('sendEmail.py', 'r', encoding='utf-8') as r:
                content = r.read()
                conn.sendall(bytes(content, encoding='utf-8'))
    conn.close()

