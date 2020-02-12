#04. 元素記号
#"Hi He Lied Because Boron Could Not Oxidize Fluorine.
#New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
# それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置
# （先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

str = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
list = str.split(' ')
one = [1,5,6,7,8,9,15,16,19]
count = 1
result = {}
for word in list:
    word = word.strip(',.')
    if count in one:
        result[word[0]] = count
    else:
        result[word[0:2]] = count
    count += 1
print(result)

#他の解答
#for (num, word) in enumerate(list, 1):
#    if num in one:
#        result[word[0:1]] = num
#    else:
#        result[word[0:2]] = num
#print(result)

'''
解説 enumerate()
引数にリストなどのイテラブルオブジェクトを指定する。
インデックス番号, 要素の順に取得できる。
デフォルトだとenumerate()関数のインデックスは0から始まる。
0以外の数値から開始したい場合は、enumerate()関数の第二引数に任意の開始数値を指定する。
例
for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie
'''