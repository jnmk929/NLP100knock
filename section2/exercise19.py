#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．
#from itertools import groupby
import collections

rfile = './hightemp.txt'
lines = []
with open(rfile,mode='r',encoding='utf_8') as f:
    for line in f:
       line = line.rstrip()
       lines.append(line.split('\t')[0])

# 都道府県で集計し、(都道府県, 出現頻度)のリスト作成
#lines.sort()
#result = [(line,len(list(group))) for line, group in groupby(lines)]
# 出現頻度でソート
#result.sort(key=lambda line: line[1],reverse=True)
#for line in result:
#    print(line[0],':',line[1])

result = collections.Counter(lines)
result = result.most_common()
for key,value in result:
    print(key,value)

'''
#!/bin/sh

# 1カラム目でソートし、重複除去して件数付きで出力、その結果をソート
cut --fields=1 hightemp.txt | sort | uniq --count | sort --reverse
'''