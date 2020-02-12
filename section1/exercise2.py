#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

pato = 'パトカー'
taku = 'タクシー'
str = []
for i in range(4):
    str.append(pato[i])
    str.append(taku[i])
str = ''.join(str)
print(str)

#解答例1
#result = ''
#for (a,b) in zip(pato,taku):
#   result += a + b
#rint(result)
#解答例2
#from functools import reduce 
#result = ''.join(reduce(lambda x, y: x + y, zip(pato, taku)))

'''
解説 zip
複数のイテラブル（リストやタプルなど）から要素を集めたリストを作るとのこと。
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
'''
'''
lambda とは 
無名関数
lambda 引数: 返り値
'''
'''
解説 functools.reduce() 
直前の結果とイテラブルから取り出した値の2つを関数に渡して新たな結果を作り、
これをイテラブルの終わりまで順次繰り返してくれます。
def add(x, y):
    return x + y 
import functools
functools.reduce(add, [1, 2, 3, 4, 5])
結果:15
'''