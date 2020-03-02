#34. 「AのB」
#2つの名詞が「の」で連結されている名詞句を抽出せよ．

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

def get_np(morp):
    np = []
    for sentence in morp:
        for i,word in enumerate(sentence):
            if word['surface'] == 'の' and i != 0 and i < len(sentence)-1:
                if sentence[i-1]['pos'] == '名詞' and sentence[i+1]['pos'] == '名詞':
                    np.append(sentence[i-1]['surface']+word['surface']+sentence[i+1]['surface'])
    return np

if __name__ == "__main__":
    morp = morpheme()
    noun = get_np(morp)
    print(noun[0:20])

#他の回答
#list_a_no_b = []        # 出現順リスト、重複あり
#lines = neco_lines()
#for line in lines:
#    if len(line) > 2:
#        for i in range(1, len(line) - 1):
#            if line[i]['surface'] == 'の' \
#                    and line[i - 1]['pos'] == '名詞' \
#                    and line[i + 1]['pos'] == '名詞':
#                list_a_no_b.append(line[i - 1]['surface'] + 'の' + line[i + 1]['surface'])
#a_no_b = set(list_a_no_b)       # 重複除去