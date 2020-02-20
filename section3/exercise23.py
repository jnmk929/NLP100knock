#23. セクション構造
#記事中に含まれるセクション名とそのレベル(例えば"== セクション名 =="なら1)を表示せよ．

import json
import re

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

category = re.findall(r'==+.*?==+',data['text'])
for c in category:
    num = int(c.count('=')/2 -1)
    print('\t'*(num-1),re.sub(r'==+? |==+','',c),':',num)
    #フォーマットが良さげ
    #c = re.sub(r'==+? |==+','',c)
    #print('{indent}{sect}:{level}'.format(indent='\t'*(num-1),sect=c,level=num))


#他の回答
# 正規表現のコンパイル
#pattern = re.compile(r'''
#    ^       # 行頭
#    (={2,}) # キャプチャ対象、2個以上の'='
#    \s*     # 余分な0個以上の空白（'哲学'や'婚姻'の前後に余分な空白があるので除去）
#    (.+?)   # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
#    \s*     # 余分な0個以上の空白
#    \1      # 後方参照、1番目のキャプチャ対象と同じ内容
#    .*      # 任意の文字が0文字以上
#    $       # 行末
#    ''', re.MULTILINE + re.VERBOSE)

# 抽出
#result = pattern.findall(data['text'])
# 結果表示
#for line in result:
#    level = len(line[0]) - 1    # '='の数-1
#    print('{indent}{sect}({level})'.format(
#        indent='\t' * (level - 1), sect=line[1], level=level))
