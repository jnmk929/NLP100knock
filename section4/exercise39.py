#39. Zipfの法則
#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

import matplotlib.pyplot as plt

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
    #日本語に対応
    plt.rcParams['font.family'] = 'IPAPGothic'
    #ファイル出力のため
    plt.figure(figsize=(6,4))
    morp = morpheme()
    count = word_count(morp)
    #print(count[::-1])

    y = list(zip(*count))[1]

    
    plt.scatter(range(1, len(y)+1), y, s=10)    #散布図 
    plt.xlim(xmin=1,xmax=len(y)+1)    #x軸の表示範囲
    plt.ylim(ymin=1,ymax=y[0])
    plt.xscale('log')   #両対数グラフ
    plt.yscale('log')

    plt.title('39 Zipfの法則')
    plt.xlabel('出現度順位')
    plt.ylabel('出現頻度')
    plt.grid(axis='both')
    plt.savefig("./data/Zipf39.jpg")    #このタイミングで出力
    plt.show()