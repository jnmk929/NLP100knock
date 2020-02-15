#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，
# 入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ

rfile = './hightemp.txt'
n = int(input('自然数を入力してください: '))
list = []
with open(rfile,mode='r',encoding='utf_8') as f:
    for line in f:
        list.append(line)

for i,line in enumerate(list):
    if i >= len(list)-n:
        print(''.join(line.replace('\n','')))


#他の回答
#readlines() で一括読み込み
# -n から で開始位置を指定
#fname = 'hightemp.txt'
#n = int(input('N--> '))

#with open(fname,'r',encoding='utf_8') as data_file:
#    lines = data_file.readlines()

# for line in lines[-n:]:
    # print(line.rstrip())

'''
#!/bin/sh

# Nを入力
echo -n "N--> "
read n

# 切り出し
tail --lines=$n hightemp.txt
'''