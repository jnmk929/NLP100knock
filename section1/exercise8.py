#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#・英小文字ならば(219 - 文字コード)の文字に置換
#・その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(sentence):
    message = []
    for chara in sentence:
        if chara.islower():
             message.append(chr(219-ord(chara)))
        else: 
            message.append(chara)
    return ''.join(message)
ango = cipher('ABcDeFgh124IjklmnOP')
huku = cipher(ango)
print(ango)
print(huku)

# 他の回答
#リスト append じゃなくて ''(文字列) で += にしたほうが好み
#def cipher(sentence):
#    message = ''
#    for chara in sentence:
#        if chara.islower():
#             message += chr(219-ord(chara))
    #    else:
#            message += chara
#    return message

#他の回答 
#これくらいなら、三項演算子がいいかも
#def cipher(sentence):
#    for chara in sentence:
#        message += chr(219 - ord(c)) if c.islower() else c

#他の回答 参考までに
#def cipher(target):
#    result = ''.join(chr(219 - ord(c)) if c.islower() else c
#                     for c in target)
#    return result