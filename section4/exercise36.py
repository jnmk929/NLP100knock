#36. 単語の出現頻度
#文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import time

def morpheme():
    with open('./data/neko.txt.mecab',mode='r',encoding='utf_8') as f:
        r = f.read()
    sentence = r.split('EOS')
    morp = []
    list = []
    for s in sentence:
        word = s.split('\n')
        for w in word:
            if w != '':
                surface = w.split('\t')[0]
                feature = w.split('\t')[1]
                base = feature.split(',')[6]
                pos = feature.split(',')[0]
                pos1 = feature.split(',')[1]
                d = {'surface':surface, 'base':base, 'pos':pos, 'pos1':pos1}
                list.append(d)
                #print('{s} : {b} : {p} : {p1}'.format(s=surface,b=base,p=pos,p1=pos1))
            if w == '' and len(list) != 0:
                morp.append(list)
                list = []
    return morp

def word_count(morp):
    count = {}
    for sentence in morp:
        for word in sentence:
            if count.get(word['surface']):
                count[word['surface']] += 1
            else:
                count[word['surface']] = 1
    #valueで降順にソート
    return sorted(count.items(),key=lambda x:x[1],reverse=True)

if __name__ == "__main__":
    morp = morpheme()
    count = word_count(morp)
    print(count[:20])

#他の回答  簡潔でよい
#カウンターオブジェクト　と　内包表現
#from collections import Counter

# Counterオブジェクトに単語をセット
#word_counter = Counter()
#for line in neco_lines():
#    word_counter.update([morpheme['surface'] for morpheme in line])