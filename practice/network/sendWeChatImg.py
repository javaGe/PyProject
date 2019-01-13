#coding=utf8
import itchat


itchat.auto_login()

# rooms=itchat.get_chatrooms(update=True)
# for i in range(len(rooms)):
#     print(rooms[i])   #查看你多有的群

# friend = itchat.search_friends(name='tester')  #这里输入你好友的名字或备注。
room = itchat.search_chatrooms(name='test') # 查找群
print(room)
userName = room[0]['UserName']
print(userName)
f='./test.png'  #图片地址
try:
    itchat.send_image(f,toUserName=userName)  #如果是其他文件可以直接send_file
    # itchat.send_msg('robot test', toUserName=userName)
    print(f)
    print("success")
except:
    print("fail")

itchat.run() # 保持在线运行