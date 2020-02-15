#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものを
# col2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

rfile = './hightemp.txt'
wfile1 = './col1.txt'
wfile2 = './col2.txt'

text = []
with open(rfile,'r',encoding='utf_8') as f:
    for line in f:
        text.append(line.split('\t'))

col1 = ''
col2 = ''
for line in text:
    col1 += line[0]+'\n'
    col2 += line[1]+'\n'

with open(wfile1,'w',encoding='utf_8') as fw1:
    fw1.write(col1)
with open(wfile2,'w',encoding='utf_8') as fw2:
    fw2.write(col2)

#他の回答
#一気にオープンするバージョン
#fname = 'hightemp.txt'
#with open(fname,'r',encoding='utf_8') as data_file, \
        # open('col1.txt', mode='w',encoding='utf_8') as col1_file, \
        # open('col2.txt', mode='w',encoding='utf_8') as col2_file:
    # for line in data_file:
        # cols = line.split('\t')
        # col1_file.write(cols[0] + '\n')
        # col2_file.write(cols[1] + '\n')

'''
#!/bin/sh

# col1の抽出と比較
cut --fields=1 hightemp.txt > col1_test.txt
diff --report-identical-files col1.txt col1_test.txt

# col2の抽出と比較
cut --fields=2 hightemp.txt > col2_test.txt
diff --report-identical-files col2.txt col2_test.txt
'''