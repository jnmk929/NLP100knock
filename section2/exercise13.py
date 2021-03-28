#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
# タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

col1 = 'col1.txt'
col2 = 'col2.txt'
marge = 'merge.txt'
with open(col1,'r',encoding='utf_8') as f1, open(col2,'r',encoding='utf_8') as f2, open(marge,'w',encoding='utf_8') as fw:
    for (c1,c2) in zip(f1,f2):
        fw.write(c1.replace('\n','')+'\t'+c2)   #rstrip()がわかりやすい 空白文字の除去


#他の回答   rs.trip()
# with open('col1.txt') as col1_file, \
        # open('col2.txt') as col2_file, \
        # open('merge.txt', mode='w') as out_file:
# 
    # for col1_line, col2_line in zip(col1_file, col2_file):
        #fw.write(c1.rstrip() + '\t' + c2.rstrip() + '\n')

'''
#!/bin/sh

# マージ
paste col1.txt col2.txt > merge_test.txt

# 比較
diff --report-identical-files merge.txt merge_test.txt
'''