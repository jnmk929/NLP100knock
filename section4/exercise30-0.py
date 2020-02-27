#30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
# 品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（
# マッピング型）のリストとして表現せよ．

import MeCab

with open('./data/neko.txt',mode='r',encoding='utf_8') as f:
    r = f.read()
neko = r.split('\n')
mecab = MeCab.Tagger()

list = []
for n in neko:
    node = mecab.parse(n)
    list.append(node)


with open('./data/neko.txt.mecab',mode='w',encoding='utf_8') as f:
    f.write(''.join(list))