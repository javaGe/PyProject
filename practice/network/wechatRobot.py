# 加载库
from itchat.content import *
import requests
import json
import itchat


# itchat.auto_login()

# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    #appkey = 'e5ccc9c7c8834ec3b08940e290ff1559'
  appkey = "227c315e49cd43d7a3d052ada17d26fc"
  url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
  # print(url)
  req = requests.get(url)
  content = req.text
  data = json.loads(content)
  answer = data['text']
  return answer


# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    print("获取到群的id: %s" % df[0]['UserName'])
    return df[0]['UserName']

# 注册文本消息，绑定到text_reply处理函数
# text_reply msg_files可以处理好友之间的聊天回复
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
  itchat.send('%s' % tuling(msg['Text']),msg['FromUserName'])

# 下载发送过来的图片和文件和视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
  msg['Text'](msg['FileName'])
  return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])


# 现在微信加了好多群，并不想对所有的群都进行设置微信机器人，只针对想要设置的群进行微信机器人，可进行如下设置
@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    # print(msg)
    # # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
    # item = group_id('test') # 根据自己的需求设置  设置群的名称
    # print("信息来源：%s" %item)

    # 如果来自设置的群就回复信息
    # if msg['FromUserName'] == item:

    # 设置需要回复的群信息
    if msg.User["NickName"] == 'test' or msg.User["NickName"] == "NB4Group":
        content = msg['Content']
        print('%s ：%s' % (msg.User["NickName"] ,content))

        reply = tuling(content)
        # itchat.send('%s' %reply, msg['FromUserName'])
        print("图灵机器人回复信息：%s" %reply)
        # 返回信息直接回复
        return reply

    elif msg['isAt']:   # 如果是其他群的消息，@本人的话也参与回复
        print('%s ：%s' % (msg.User["NickName"] ,msg['Content']))
        return tuling(msg['Content'])

    else:
        pass

itchat.auto_login()
# 获取所有通讯录中的群聊
# 需要在微信中将需要同步的群聊都保存至通讯录
chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
chatroom_ids = [c['UserName'] for c in chatrooms]
print('正在监测的群聊：', len(chatrooms), '个')
print(' '.join([item['NickName'] for item in chatrooms]))
# 开始监测
itchat.run()