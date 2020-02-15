#18. 各行を3コラム目の数値の降順にソート
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）
#確認にはsortコマンドを用いよ

rfile = './hightemp.txt'
lines = []
with open(rfile,mode='r',encoding='utf_8') as f:
    for line in f:
       line = line.rstrip()
       lines.append(line.split('\t'))

lines[2].sort(reverse=True) #指定位置でソート
for line in lines:
    print('\t'.join(line))

#他の回答
#fname = 'hightemp.txt'
#lines = open(fname,'r',encoding='utf_8').readlines()
#lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

#for line in lines:
#    print(line, end='')

'''

# 3カラム目を数値として逆順ソート
sort hightemp.txt --key=3,3 --numeric-sort --reverse > result_test.txt

# Pythonのプログラムで実行
python main.py > result.txt

# 結果の確認
diff --report-identical-files result.txt result_test.txt
'''