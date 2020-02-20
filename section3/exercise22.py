#22. カテゴリ名の抽出
#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json
import re

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

category = re.findall(r'\[\[Category:.+\]\]',data['text'])

for c in category:
    c = re.sub(r'\[\[Category:','',c)
    #c = re.sub(r'\|?\*?\]\]','',c)
    c = re.sub(r'\|.*\]\]|\]\]','',c)
    print(c)

#他の回答
# 正規表現のコンパイル
#pattern = re.compile(r'''
#    ^       # 行頭
#    .*      # 任意の文字0文字以上
#    \[\[Category:
#    (       # キャプチャ対象のグループ開始
#    .*?     # 任意の文字0文字以上、非貪欲マッチ（貪欲にすると後半の'|'で始まる装飾を巻き込んでしまう）
#    )       # グループ終了
#    (?:     # キャプチャ対象外のグループ開始
#    \|.*    # '|'に続く0文字以上
#    )?      # グループ終了、0か1回の出現
#    \]\]
#    .*      # 任意の文字0文字以上
#    $       # 行末
#    ''', re.MULTILINE + re.VERBOSE)
#
# 抽出
#result = pattern.findall(data)

# 結果表示
#for line in result:
#    print(line)

#他の回答 こっちが直感的
#import re
#head_pattern = r'\[\[Category:'
#tail_pattern = r'\|?\*?\]\]'
#for l in obj['text'].split('\n'):
#    if 'Category' in l:
#        l = re.sub(head_pattern, '', l)
#        print(re.sub(tail_pattern, '', l))