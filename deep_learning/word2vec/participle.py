import os
import jieba.posseg

txt_path = r'D:\ic_files\TXT\20170926\0c7a0cec-a332-11e7-96b7-408d5c0b8e74_done.txt'
with open(txt_path, 'r', encoding='utf-8') as r:
    lines = r.readlines()
for line in lines:
    words = jieba.posseg.cut(line)
    for word in words:
        print(str(word))