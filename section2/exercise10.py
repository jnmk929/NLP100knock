#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．

with open('./hightemp.txt',mode='r',encoding='utf_8') as f:
    r = f.read()

count = 0
for moji in r:
    if moji == '\n':
        count += 1
print(count)

#他の回答 with の中で 行で読み込む
'''
fname = 'hightemp.txt'
count = 0
with open(fname,encoding='utf_8') as data_file:
    for line in data_file:
        count += 1
print(count)
'''
'wc hightemp.txt'