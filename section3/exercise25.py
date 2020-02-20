#25. テンプレートの抽出
#記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．

import json
import re

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

#正規表現の参考サイト
#https://hibiki-press.tech/learn_prog/python/regex_pattern/1099#i-7
#category = re.findall(r'\{\{基礎情報 (.*?)^\}\}',data['text'],re.MULTILINE+re.DOTALL)

category = re.findall(r'\{\{基礎情報 (.*)^\}\}',data['text'],re.MULTILINE+re.DOTALL)
category = category[0].split('\n|')
d = {}
for c in category:
    c = c.replace('\n','')
    template = c.split(' = ')     #keyとvalueに分ける
    if len(template) >= 2:      #最初の国を取り除く
        d[template[0]] = template[1] 
print(d.values())

#他の回答
# 基礎情報テンプレートの抽出条件のコンパイル
#pattern = re.compile(r'''
#    ^\{\{基礎情報.*?$   # '{{基礎情報'で始まる行
#    (.*?)       # キャプチャ対象、任意の0文字以上、非貪欲
#    ^\}\}$      # '}}'の行
#    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# 基礎情報テンプレートの抽出
#contents = pattern.findall(data['text'])

# 抽出結果からのフィールド名と値の抽出条件コンパイル
#pattern = re.compile(r'''
#    ^\|         # '|'で始まる行
#    (.+?)       # キャプチャ対象（フィールド名）、任意の1文字以上、非貪欲
#    \s*         # 空白文字0文字以上
#    =
#    \s*         # 空白文字0文字以上
#    (.+?)       # キャプチャ対象（値）、任意の1文字以上、非貪欲
#    (?:         # キャプチャ対象外のグループ開始
#        (?=\n\|)    # 改行+'|'の手前（肯定の先読み）
#        | (?=\n$)   # または、改行+終端の手前（肯定の先読み）
#    )           # グループ終了
#    ''', re.MULTILINE + re.VERBOSE + re.DOTALL)

# フィールド名と値の抽出
#fields = pattern.findall(contents[0])

# 辞書にセット
#result = {}
#keys_test = []      # 確認用の出現順フィールド名リスト
#for field in fields:
#    result[field[0]] = field[1]
#    keys_test.append(field[0])

# 確認のため表示（確認しやすいようにkeys_testを使ってフィールド名の出現順にソート）
#for item in sorted(result.items(),
#        key=lambda field: keys_test.index(field[0])):
#    print(item)