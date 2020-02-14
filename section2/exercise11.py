#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ．

file = './hightemp.txt'
sentence = ''
with open(file,encoding='utf_8') as f:
    for line in f:
        sentence += line.replace('\t',' ')
print(sentence)

#他の回答
#fname = 'hightemp.txt'
#with open(fname) as data_file:
#    for line in data_file:
#        print(line.replace('\t', ' '), end='')

'''
# sedのsコマンド： s/検索パターン/置換文字列/g（すべて置換）
sed 's/\t/ /g' .\hightemp.txt
'''