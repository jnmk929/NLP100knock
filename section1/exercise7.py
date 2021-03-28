#07. テンプレートによる文生成
#数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

#題意とは違う感じが、、
x = 12
y = '気温'
z = 22.4
#print(x,'時の',y,'は',z)
print('{}時の{}は{}'.format(x,y,z))

#他の回答 フォーマット
#print('{hour}時の{target}は{value}'.format(hour=x,target=y,value=z))

#他の回答 string.Template
#from string import Template
#temp = Template('$hour時の$targetは$value')
#print(temp.substitute(hour=x,target=y,value=z))

#他の回答 python3.6以上
#print(f'{x}時の{y}は{z}')