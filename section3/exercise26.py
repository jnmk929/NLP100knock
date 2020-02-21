#26. 強調マークアップの除去
#25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
#(弱い強調，強調，強い強調のすべて)を除去してテキストに変換せよ

import json
import re

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

pattern = re.compile(r'\{\{基礎情報\s*(.*)^\}\}',re.MULTILINE+re.DOTALL)
category = pattern.findall(data['text'])
#category = re.findall(r'\{\{基礎情報 (.*)^\}\}',data['text'],re.MULTILINE+re.DOTALL)
pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)^',re.MULTILINE+re.DOTALL)
template = pattern.findall(category[0])
dict = {}
for key,val in template:
    val = re.sub('\n','',val)
    val = re.sub(r"\'{2,5}",'',val)
    dict[key] = val
for key,val in dict.items():
    print('{k} : {v}'.format(k=key,v=val))
