#27. 内部リンクの除去
#26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去
#し，テキストに変換せよ

import json
import re

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

pattern = re.compile(r'\{\{基礎情報\s*(.*)^\}\}',re.MULTILINE+re.DOTALL)
category = pattern.findall(data['text'])
#category = re.findall(r'\{\{基礎情報 (.*)^\}\}',data['text'],re.MULTILINE+re.DOTALL)
#pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(\n\||\n$)',re.MULTILINE+re.DOTALL)
#pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)^',re.MULTILINE+re.DOTALL+re.VERBOSE)
pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', re.MULTILINE + re.DOTALL)
template = pattern.findall(category[0])
#print(template)
dict = {}
for key,val in template:
    val = re.sub('\n','',val)
    val = re.sub(r"\'{2,5}",'',val)
    val = re.sub(r'\[\[|\]\]','',val)
    dict[key] = val

for key,value in dict.items():
    print('{k} : {v}'.format(k=key,v=value))