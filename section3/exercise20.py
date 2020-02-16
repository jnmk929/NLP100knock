#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
# 問題21-29では，ここで抽出した記事本文に対して実行せよ．

#・1行に1記事の情報がJSON形式で格納される
#・各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，
#  そのオブジェクトがJSON形式で書き出される
import json

country = './data/country.json'
data = []
with open(country,'r',encoding='utf_8') as j:
    for line in j:
        wiki = json.loads(line)
        if wiki['title'] == 'イギリス':
            #print(wiki['text'])
            data = wiki
#以降のためにファイル書き込み
england ='./data/great_britain.json'
with open(england,'w',encoding='utf_8') as f:
    json.dump(data,f,ensure_ascii=False)

#他の回答
#import gzip
#import json
#fname = 'jawiki-country.json.gz'       <- ファイルの解凍からしてる

#with gzip.open(fname, 'rt') as data_file:
#    for line in data_file:
#        data_json = json.loads(line)
#        if data_json['title'] == 'イギリス':
#            print(data_json['text'])
#            break