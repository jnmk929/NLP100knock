#00. 文字列の逆順
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

str = "stressed"
print("str:",str)

r_str1 = str[::-1]      #スライス
print("r_str1:",r_str1)

r_str2 = ''.join(list(reversed(str)))     #イテレータをリストに変換した後
print("r_str2:",r_str2)
