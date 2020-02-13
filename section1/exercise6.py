#06. 集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(list,n):
    gram = []
    for i in range(len(list) - n + 1):
        gram.append(list[i:i+n])    
    return gram

x = 'paraparaparadise'
y = 'paragraph'

x_bi = n_gram(x,2)
y_bi = n_gram(y,2)
print('x_bi:',x_bi)
print('y_bi:',y_bi)

#和集合
wa = x_bi + y_bi
xy_or = []
for w in wa:
    if(not(w in xy_or)):
        xy_or.append(w)
print('or:',xy_or)

#積集合
xy_and = []
for x in x_bi:
    if x in y_bi and not(x in xy_and):
        xy_and.append(x)
print('and:',xy_and)

#差集合
xy_diff = []
for o in xy_or:
    if not o in x_bi:
        xy_diff.append(o)
print('diff',xy_diff)

#seが含まれるかどうか
if 'se' in x_bi:
    print('x_bi:true')
if 'se' in y_bi:
    print('y_bi:true')

#他の回答1
#集合を表すデータ型 set を使う
# 集合の作成
set_x = set(n_gram('paraparaparadise', 2))
print('X:' + str(set_x))
set_y = set(n_gram('paragraph', 2))
print('Y:' + str(set_y))

# 和集合
set_or = set_x | set_y
print('和集合:' + str(set_or))

# 積集合
set_and = set_x & set_y
print('積集合:' + str(set_and))

# 差集合
set_sub = set_x - set_y
print('差集合:' + str(set_sub))

# 'se'が含まれるか？
print('seがXに含まれる:' + str('se' in set_x))
print('seがYに含まれる:' + str('se' in set_y))