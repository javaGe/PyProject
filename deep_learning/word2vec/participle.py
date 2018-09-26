import os
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# txt_path = r'D:\ic_files\TXT\20170926\0c7a0cec-a332-11e7-96b7-408d5c0b8e74_done.txt'
# with open(txt_path, 'r', encoding='utf-8') as r:
#     lines = r.readlines()
# for line in lines:
#     words = jieba.posseg.cut(line)
#     for word in words:
#         print(str(word))

'''
对语句进行分词然后生成词云
'''

contents = '看到了房间爱家的金佛阿加几个啊发偶奇偶节疯狂佛那就发了发哦杰伦爱国家里发链接发来阿卡疯了啊啊'
with open('测试.txt', 'r', encoding='utf-8')as r:
    contents = r.read()

contents_rank = jieba.analyse.extract_tags(contents, topK=30, withWeight=True)
key_words = dict()
for i in contents_rank:
    key_words[i[0]] = i[1]
print(key_words)
wc = WordCloud(font_path='C:/Windows/Fonts/simhei.ttf', background_color='White', max_words=40)
wc.generate_from_frequencies(key_words)
plt.imshow(wc)
plt.axis('off')
plt.show()