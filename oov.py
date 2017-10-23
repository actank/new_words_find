#coding:utf-8

import sys
import pickle
import math

origin_freq = {}
new_freq = {}
freezing = {}
freedom = {}
l_dict = {}
r_dict = {}
#统计左右邻，左右熵(自由度)，互信息，凝固度

def get_3_gram(l):
    ll = []
    i = 3
    while i >= 0:
        if len(l) < i:
            i = i - 1
            continue
        for j in range(len(l) - i):
            s = l[j]
            for k in range(j + 1,j + i + 1):
                s = s + "#" + l[k]
            if s not in ll:
                ll.append(s)
                if s not in origin_freq:
                    origin_freq.setdefault(s, 1)
                else:
                    origin_freq[s] += 1
        i = i - 1
    return ll

def cal_freezing():
    return

def cal_freq():
    f = open("./train_data") 
    for line in f:
        l = line.strip().split(" ")
        ll = get_3_gram(l)
    f1 = open('origin_freq.pkl', 'wb')
    pickle.dump(origin_freq, f1)
    f.close()
    return

def find_new_words():
    pkl_file = open('origin_freq.pkl', 'rb')
    origin_freq = pickle.load(pkl_file)
    count = 0.0
    for item in origin_freq:
        count += float(origin_freq[item])
        #很挫的方法对3/4gram统计左右连接词map
        ll = item.strip().split("#")
        if len(ll) >= 3:
            l_k = "#".join(ll[1:])
            r_k = "#".join(ll[:-1])
            if l_k in l_dict:
                if not ll[0] in l_dict[l_k]:
                    l_dict[l_k].append(ll[0])
            else:
                l_dict[l_k] = [ll[0]]
            if r_k in r_dict:
                if not ll[-1] in r_dict[r_k]:
                    r_dict[r_k].append(ll[-1])
            else:
                r_dict[r_k] = [ll[-1]]
            
    for item in origin_freq:
        if not '#' in item:
            continue
        freq = origin_freq[item]
        item = item.strip()
        words = item.split("#")
        if len(words) == 2:
            freezing[item] = freq / count
            word1 = words[0]
            word2 = words[1]
            pa = origin_freq[word1] / count
            pb = origin_freq[word2] / count
            if not freezing[item] > (pa * pb * 1000):
                continue
            left_entropy = 0.0
            right_entropy = 0.0
            if item not in l_dict or item not in r_dict:
                continue
            for k in l_dict[item]:
                tmp = origin_freq[k + "#" + item] / origin_freq[item]
                left_entropy += (0.0 - tmp * math.log(tmp, 2))
            for k in r_dict[item]:
                tmp = origin_freq[item + "#" + k] / origin_freq[item]
                #if tmp < 0:
                #    print(k+"#"+item, item, origin_freq[k+"#"+item], origin_freq[item])
                right_entropy += (0.0 - tmp * math.log(tmp, 2))
            if left_entropy > 0.2 and right_entropy > 0.2:
                print(item, left_entropy, right_entropy)
                
            
            #print(item, freezing[item], pa, pb, pa*pb*10)


    return

if __name__ == "__main__":
    #cal_freq()
    find_new_words()
