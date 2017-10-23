#coding:utf-8
import word2vec


def get_synonmys():
    model = word2vec.load('./model.bin')
    with open("./tf_dict") as f:
        for w in f:
            w = w.strip()
            try:
                indexes, metrics = model.cosine(w)
                for i in zip(indexes, metrics):
                    word = model.vocab[i[0]]
                    sim = i[1]
                    if sim>0.85 and sim<0.95:
                        print("%s %s %f" % (w,word,sim))
            except Exception as e:
                continue
    return

if __name__ == "__main__":
    get_synonmys()
