#第5章: 係り受け解析
#夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
# その結果をneko.txt.cabochaというファイルに保存せよ．

import CaboCha

with open('./data/neko.txt',mode='r',encoding='utf_8') as fr:
    r = fr.read()

neko = r.split('\n')
cabocha = CaboCha.Parser()

l = []
for s in neko:
    tree = cabocha.parse(s)
    l.append(tree.toString(CaboCha.FORMAT_LATTICE))

with open('./data/neko.txt.cabocha',mode='w',encoding='utf_8') as fw:
    fw.write(''.join(l))