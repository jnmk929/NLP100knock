#30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
# ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
# 品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（
# マッピング型）のリストとして表現せよ．

import MeCab
import time

with open('./data/neko.txt.mecab',mode='r',encoding='utf_8') as f:
    r = f.read()
sentence = r.split('EOS')

result = []
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
            result.append(list)
            list = []
            #list.clear() <- result の要素がなくなる
            #参考サイト
            #https://it-for-pharma.com/python-%E3%83%AA%E3%82%B9%E3%83%88%E3%81%AE%E8%A6%81%E7%B4%A0%E3%82%92%E6%B6%88%E3%81%99%E9%9A%9B%E3%81%AEclear%E9%96%A2%E6%95%B0%E3%81%AE%E6%B3%A8%E6%84%8F%E7%82%B9%E3%81%A8%E5%AF%BE%E7%AD%96
print(result)

#他の回答
#もうそろそろ関数つくるか
# 第4章: 形態素解析
#import re

#def analyze():
#    lines = []
#    sentence = []
#    with open('./data/neko.txt.mecab', 'r', encoding='utf8') as fin:
#        for line in fin:
#            words = re.split(r'\t|,|\n', line)
#            if words[0] == 'EOS':
#                if sentence:
#                    lines.append(sentence)
#                    sentence = []
#                continue
#            sentence.append({
#                "surface": words[0],
#                "base": words[7],
#                "pos": words[1],
#                "pos1": words[2],
#            })
#    return lines

#def main():
#    article = analyze()
#    print(article[0])
#    print()
#    print(article[1])
#    print()
#    print(article[2])

#if __name__ == '__main__':
#    main()

#他の回答
#def neco_lines():
#    '''「吾輩は猫である」の形態素解析結果のジェネレータ
#    「吾輩は猫である」の形態素解析結果を順次読み込んで、各形態素を
#    ・表層形（surface）
#    ・基本形（base）
#    ・品詞（pos）
#    ・品詞細分類1（pos1）
#    の4つをキーとする辞書に格納し、1文ずつ、この辞書のリストとして返す
#
#    戻り値：
#    1文の各形態素を辞書化したリスト
#    '''
#    with open(fname_parsed) as file_parsed:
#
#        morphemes = []
#        for line in file_parsed:
#
#            # 表層形はtab区切り、それ以外は','区切りでバラす
#            cols = line.split('\t')
#            if(len(cols) < 2):
#                raise StopIteration     # 区切りがなければ終了
#            res_cols = cols[1].split(',')
#
#            # 辞書作成、リストに追加
#            morpheme = {
#                'surface': cols[0],
#                'base': res_cols[6],
#                'pos': res_cols[0],
#                'pos1': res_cols[1]
#            }
#            morphemes.append(morpheme)
#
#            # 品詞細分類1が'句点'なら文の終わりと判定
#            if res_cols[1] == '句点':
#                yield morphemes
#                morphemes = []