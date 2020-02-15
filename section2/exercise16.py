#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位で
# N分割せよ．同様の処理をsplitコマンドで実現せよ
import math
rfile = './hightemp.txt'
n = int(input('自然数を入力してください: '))
with open(rfile,mode='r',encoding='utf_8') as f:
    lines = f.readlines()

out = math.ceil(len(lines)/n)


for i,line in enumerate(lines):
        print(line.replace('\n',''))
        if i % out == out - 1:
            print('='*14)

#他の回答
#問題文が分かりづらい
#print('------\n'.join([''.join(lines[i * n:(i + 1) * n]) for i in range(0, math.ceil(len(lines) / n))]))


#他の回答
#import math

#fname = 'hightemp.txt'
#n = int(input('N--> '))

#with open(fname) as data_file:
#    lines = data_file.readlines()

#count = len(lines)
#unit = math.ceil(count / n)  # 1ファイル当たりの行数

#for i, offset in enumerate(range(0, count, unit), 1):
#    with open('child_{:02d}.txt'.format(i), mode='w') as out_file:
#        for line in lines[offset:offset + unit]:
#            out_file.write(line)
