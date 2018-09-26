from gensim.models import word2vec

# sentences = word2vec.Text8Corpus("测试.txt")
# moduel_ = word2vec.Word2Vec.load("D:\\mySoftWare\\10G训练好的词向量\\60维\\Word60.model")
#
# y = moduel_.similarity('河南', '北京')
# print(y)

import os
path = r'D:\ic_files\TXT'
text_lis = []
dirs = os.listdir(path)
for dir in dirs:
    text_path = path + "\\" + dir
    texts = os.listdir(text_path)
    text_lis.extend(texts)
print(text_lis.__len__())