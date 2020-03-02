#35. 名詞の連接
#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
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

def get_long_noun(morp):
    noun = ''
    result = []
    for sentence in morp:
        for word in sentence:
            if word['pos'] == '名詞':
                noun += word['surface']
                one_word = word['surface']
            elif noun != '' and noun != one_word:
                result.append(noun)
                noun = ''
            else:
                noun = ''
    return result

if __name__ == "__main__":
    morp = morpheme()
    noun = get_long_noun(morp)
    print(noun[0:40])

#他の回答 だいたい一緒
# 1文ずつ辞書のリストを取得し抽出
#list_series_noun = []       # 出現順リスト、重複あり
#for line in neco_lines():
#    nouns = []      # 見つけた名詞のリスト
#    for morpheme in line:

#        # 名詞ならnounsに追加
#        if morpheme['pos'] == '名詞':
#            nouns.append(morpheme['surface'])

        # 名詞以外なら、それまでの連続する名詞をlist_series_nounに追加
#        else:
#            if len(nouns) > 1:
#                list_series_noun.append("".join(nouns))
#            nouns = []

    # 名詞で終わる行があった場合は、最後の連続する名詞をlist_series_nounに追加
#    if len(nouns) > 1:
#        list_series_noun.append("".join(nouns))