#24. ファイル参照の抽出
#記事から参照されているメディアファイルをすべて抜き出せ．
#ファイルかFileに当たるものらしい

import json
import re

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

category = re.findall(r'(ファイル|File):(.*?)\|',data['text'])
#メディアファイルの定義がばらばら
#category = re.findall(r'\[\[(ファイル|File):(.*?)\|+.*?\]\]',data['text'])

for f,c in category:
    print(c)

#他の回答
#正規表現のコンパイル
#pattern = re.compile(r'''
#    (?:File|ファイル)   # 非キャプチャ、'File'か'ファイル'
#    :
#    (.+?)   # キャプチャ対象、任意の文字1文字以上、非貪欲
#    \|
#    ''', re.VERBOSE)

# 抽出
#result = pattern.findall(data['text'])

# 結果表示
#for line in result:
#    print(line)

#他の回答
#text = data['text']
#reg = re.compile(r'\[\[File:(?P<fname>.+?)\|')
# print([reg.match(line).group('fname') for line in text.split('\n') if reg.match(line) is not None])
#for line in text.split('\n'):
#    result = reg.match(line)
#    if result is None:
#        continue
#    print(result.group('fname'))