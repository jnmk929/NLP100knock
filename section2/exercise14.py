#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

n = int(input('自然数を入力してください'))
rfile = './hightemp.txt'
with open(rfile,mode='r',encoding='utf_8') as f:
    for i,line in enumerate(f):
        if i < n:
            print(line)      #rstrip()で無駄を省いてもいいかも


#他の回答
#fname = 'hightemp.txt'
#n = int(input('N--> '))
#
#with open(fname) as data_file:
#    for i, line in enumerate(data_file):
#        if i >= n:
            # break
        # print(line.rstrip())

#他の回答
# coding: utf-8

#fname = 'hightemp.txt'
#n = int(input('N--> '))
#
#with open(fname) as lines:
#    for i in range(n):
#        print(next(lines), end='')

'''
#!/bin/sh

# Nを入力
echo -n "N--> "
read n

# 切り出し
head --lines=$n hightemp.txt
'''