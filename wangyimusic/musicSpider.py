'''下载网易云抖音音乐'''
import time
import urllib

import requests

'''
下载步骤：
1.获取所有音频的id
2.通过外链进行下载
外链地址：
http://music.163.com/song/media/outer/url?id=
加上id.mp3
483671599.mp3
'''
# 创建一个音乐实体类
class Music163(object):
    # 初始化时设置参数
    def __init__(self):
        self.headers = {
            'Cookie':'ail_psc_fingerprint=489a1ee9a8838699a1e50094226ee8a4; _iuqxldmzr_=32; _ntes_nnid=93e8a356b1355868c04b956990895dc3,1528856902905; _ntes_nuid=93e8a356b1355868c04b956990895dc3; usertrack=O2+gylssv1AZjDMaAwNwAg==; WM_TID=o%2BN0Am0Tj3zrdpaUwYpOvIIUhUu0DDpJ; Province=0530; City=0531; nts_mail_user=ytbfzd@163.com:-1:1; __f_=1537065092272; NNSSPID=2d4a0bd0bb7641e8b345ea0c28b13f07; P_INFO=liuyanjun00@163.com|1537171727|0|other|11&20|PL&1537108625&other#shd&null#10#0#0|&0|urs&mail163|liuyanjun00@163.com; __utmz=94650624.1537193819.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=ldWHA1%2FVfjsC6CpwOdUY2uT5kKgPyJodZNQ%2F9pKUEWSOq7iGdRvBtBqwjIg%2FlZv2byFdEENVQmdn5SC%2F%5CjidN6SwrwK1wrQxs7DSZeVk0ica8flJ%2BvZ5XwqegGCB15k2w1DJZi%5Ckg%5C%2FzelH%5CO3gbp4YDrUUFtDKw0e9flvpkxyiwYSSy%3A1537231432828; __utma=94650624.1665018979.1537182135.1537193819.1537229634.5; __utmc=94650624; WM_NI=PwK44TRiLJVeuiUDWV2%2B92xNPB4%2FFGGvOObYXQsAcZr06B3lb07xuEZGJF1tO0ElsH9i6GpP1LA94F7xGt%2FA8IA1wlLeGs1wNn9L1pMvWBY1CHHr1%2BXUVOO71bJj34zEVXI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeafc2739898ab83b83ea5b084d2e972f8f58dabcc6f9be9f8a2d033a99aa695db2af0fea7c3b92a94a985d5b76092b784abd56fb7b79ba5d65ef2f5f7d3fb46949efcd0c54d85aa81b0e1539c8fbda2e252b2f0faa3b268a2f0f999f84f9a9986a7b4808df08b8df244fbb7faa8f35cf3948fdab74ef5a88995ae4bfc978fd2f66890bb8994b47d8eb2f7adb47c8faa99a3dc3b81988893b4219c8b9ab0ce3df3be868bb240ba9b9ab9cc37e2a3; __utmb=94650624.11.10.1537229634',
            'Referer':'https://music.163.com/'
        }

        # 初始化一个存储id的List
        #self.id_list = []


    def download(self, rsp):
        # 获取每页的音频
        page_data = rsp.json()['result']['songs']

        # 获取id和name
        for data in page_data:
            id = data['id']
            print('id=' + str(id))

            name = data['name']
            print('name=' + name)
            try:
                # 使用urllib模块下载音频文件urllib.request.urlretrieve（url, savepath） url:音乐链接，savepath:音频保存路径
                urllib.request.urlretrieve('http://music.163.com/song/media/outer/url?id=' + str(id) + '.mp3', 'D:/Program Files (x86)/Netease/音乐/douyin/' + name +'.mp3')
                time.sleep(2)
            except Exception as e:
                continue
    def get_songs_list(self):
        url = r'http://music.163.com/api/search/pc'
        page = 0
        dispage = 30
        while True:
            data = {
                's': '抖音',
                'offset': str(page),
                'limit': str(dispage),
                'type': '1'
            }
            response = requests.post(url, headers=self.headers, data=data)
            if response.status_code == 200:
                if 'songs' in response.json()['result'].keys():
                    print('正在获取第%d页歌曲列表' % page)
                    self.download(response)
                else:
                    print('歌曲获取完毕')
                    break
            else:
                print('访问失败')
                break
            page += 30
            time.sleep(3)

def main():
    music163 = Music163()
    music163.get_songs_list()


if __name__ == '__main__':
    main()

'''
下载音频方式：
1、
import requests 

req = requests.get('http://music.baidu.com/data/music/file?link=&song_id=1128053'.decode('utf-8'))  

with open('C:/冰雨.mp3'.decode('utf-8'), 'wb') as code:
      code.write(req.content)

'''

# 使用urllib模块下载音频文件urllib.request.urlretrieve（url, savepath） url:音乐链接，savepath:音频保存路径
urllib.request.urlretrieve('http://music.163.com/song/media/outer/url?id=436514312.mp3', 'd:/成都.mp3')