#coding:utf-8

import sys
import os
import jieba
import re

brand_dict = {}

def check_contain_chinese(check_str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
def load_brand_dict():
    with open("./brand_ext.dic") as f:
        for line in f:
            line = line.strip()
            brand_dict[line] = 1
    return
def clean():
    jieba.load_userdict('userdict.txt')
    g_pattern = re.compile("[0-9]{1,10}(ml|ML|g|cc|x2|x5|k|G)$")
    n_pattern = re.compile(r"^(-?\d+)(\.\d*)?$")
    black_dict = ['新款','爆款','男款','男士','女款','女士','男式','女式','男','女','配以','最最','个月量','万用','不伤','不怕','镇店之宝']
    num_dict = ['一','二','三','四','五','六','七','八','九','十']

    f_out = open("./train_data", "w")
    with open("./goods_name") as f:
        for line in f:
            seg_words = jieba.cut(line)
            final_words = []
            for word in seg_words:
                if len(word) == 1:
                    continue
                if word.isdigit():
                    continue
                if g_pattern.match(word):
                    continue
                if n_pattern.match(word):
                    continue
                if word in black_dict:
                    continue
                #去掉纯英文
                if not check_contain_chinese(word):
                    continue
                #去掉品牌词
                if word in brand_dict:
                    continue
                num_flag = True
                for w in word:
                    if w in num_dict:
                        num_flag = False
                        break
                if not num_flag:
                    continue
                final_words.append(word)
            f_out.write(" ".join(final_words))
            f_out.write("\n")
    f_out.close()
    return


if __name__ == "__main__":
    clean()
