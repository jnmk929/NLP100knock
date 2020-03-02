#33. サ変名詞
#サ変接続の名詞をすべて抽出せよ．

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

def get_sahen_noun(morp):
    noun = []
    for sentence in morp:
        for word in sentence:
            if word['pos1'] == 'サ変接続':
                noun.append(word['surface'])
    return noun

if __name__ == "__main__":
    morp = morpheme()
    noun = get_sahen_noun(morp)
    print(noun[0:10])