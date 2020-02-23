#29. 国旗画像のURLを取得する
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．
#（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

import json
import re
import urllib.parse, urllib.request
import requests

country = './data/great_britain.json'
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        data = json.loads(line)

pattern = re.compile(r'\{\{基礎情報\s*(.*)^\}\}',re.MULTILINE+re.DOTALL)
category = pattern.findall(data['text'])
pattern = re.compile(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', re.MULTILINE + re.DOTALL)
template = pattern.findall(category[0])
dict = {}
for key,val in template:
    val = re.sub('\n','',val)
    val = re.sub(r"\'{2,5}",'',val)
    val = re.sub(r'\[\[|\]\]','',val)
    val = re.sub(r'<ref>|</ref>|<br />|<br/>|<ref.*?/>|\(&.*?\)|<ref.*?>|\[.*?\]','',val)
    dict[key] = val

#素人の言語処理100本ノックより
#https://qiita.com/segavvy/items/fc7257012d8a590185e5

# リクエスト生成
url = 'https://www.mediawiki.org/w/api.php?action=query&titles=File:{file}&format=json&prop=imageinfo&iiprop=url'
url = url.format(file=dict['国旗画像'])
headers = {'User-Agent': 'NLP100_Python(@segavvy)'}

# MediaWikiのサービスへリクエスト送信
r = requests.get(url,headers=headers)

# jsonとして受信
data = json.loads(r.text)

# URL取り出し
print(data['query']['pages']['-1']['imageinfo'][0]['url'])

#他の回答
# 国旗画像の値を取得
#fname_flag = result['国旗画像']

# リクエスト生成
#url = 'https://www.mediawiki.org/w/api.php?' \
#    + 'action=query' \
#    + '&titles=File:' + urllib.parse.quote(fname_flag) \
#    + '&format=json' \
#    + '&prop=imageinfo' \
#    + '&iiprop=url'

# MediaWikiのサービスへリクエスト送信
#request = urllib.request.Request(url,
#    headers={'User-Agent': 'NLP100_Python(@segavvy)'})
#connection = urllib.request.urlopen(request)

# jsonとして受信
#data = json.loads(connection.read().decode())

# URL取り出し
#url = data['query']['pages'].popitem()[1]['imageinfo'][0]['url']