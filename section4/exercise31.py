#31. 動詞
#動詞の表層形(surface)をすべて抽出せよ．

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

def get_verb_surface(morp):
    verb = []
    for sentence in morp:
        for word in sentence:
            if word['pos'] == '動詞':
                verb.append(word['surface'])
    return verb

if __name__ == "__main__":
    morp = morpheme()
    verb = get_verb_surface(morp)
    print(verb[0:10])

#他の回答
#重複を防ぐため　set を使ってる
#for line in morp:
#    for mo in line:
#        if mo['pos'] == '動詞':
#            verbs.add(mo['surface'])
#            verbs_test.append(mo['surface'])      # 確認用の出現順リストにも追加