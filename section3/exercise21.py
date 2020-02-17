#21. カテゴリ名を含む行を抽出
#記事中でカテゴリ名を宣言している行を抽出せよ．

import json
import re

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

#正規表現で Category を抽出
category = re.findall(r'\[\[Category:.*?\]\]',data['text'])
for c in category:
    print(c)

#他の回答
#少々ややこしい気が...
# 正規表現のコンパイル
#pattern = re.compile(r'''
#    ^   # 行頭
#    (   # キャプチャ対象のグループ開始
#    .*  # 任意の文字0文字以上
#    \[\[Category:
#    .*  # 任意の文字0文字以上
#    \]\]
#    .*  # 任意の文字0文字以上
#   )   # グループ終了
#    $   # 行末
#    ''', re.MULTILINE + re.VERBOSE)
# 抽出
#result = pattern.findall(data['text'])
