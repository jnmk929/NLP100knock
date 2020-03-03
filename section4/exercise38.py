#38. ヒストグラム
#単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数
#を棒グラフで表したもの）を描け．

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

    x = []
    for key,value in count:
        x.append(value)
    #x = list(zip(*count))[1]

    plt.hist(x,bins=30,range=(0,30),ec='black') # 表示する棒:30 最小と最大の範囲:30 縁の色:black
    plt.xlim(xmin=1,xmax=30)    #x軸の表示範囲
    plt.title('38 ヒストグラム')
    plt.xlabel('出現回数')
    plt.ylabel('出現した文字の種類数')
    plt.grid(axis='y')
    plt.savefig("./data/histgram38.jpg")    #このタイミングで出力
    plt.show()