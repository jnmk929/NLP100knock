#09. Typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の
# 文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の
# 単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that 
# I could actually understand what I was reading : the phenomenal power of
# the human mind ."）を与え，その実行結果を確認せよ．

import random
str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(str)
words = str.split(' ')
result = []
for word in words:
    if len(word) <= 3:
        result.append(word)
    else:
        shu = list(word[1:-1])     #配列の2番目以降と最後から一つ前      len(word)-1 = -1
        random.shuffle(shu)
        result.append(word[0] + ''.join(shu) + word[-1])
typo = ' '.join(result)
print(typo)


