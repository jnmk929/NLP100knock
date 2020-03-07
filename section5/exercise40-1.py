#40. 係り受け解析結果の読み込み（形態素）
#形態素を表すクラスMorphを実装せよ．このクラスは表層形(surface),基本形(base),
#品詞(pos),品詞細分類1(pos1)をメンバ変数に持つこととする．
#さらに，CaboChaの解析結果(neko.txt.cabocha)を読み込み，
#各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

class Morph:
    surface = None
    base = None
    pos = None
    pos1 = None

    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def get_morph(self):
        return 'surface:{}\tbase:{}\tpos:{}\tpos1:{}'.format(self.surface,self.base,self.pos,self.pos1)

    def __str__(self):
        return 'surface:{}\tbase:{}\tpos:{}\tpos1:{}'.format(self.surface,self.base,self.pos,self.pos1)

def word_analysis(depend):
    sentence = []
    word = []
    for d in depend.split('\n'):
        if (not d in 'EOS') and d[0] != '*':
            surface = d.split('\t')[0]
            feature = d.split('\t')[1].split(',')   #特徴部分を抽出
            base = feature[6]
            pos = feature[0]
            pos1 = feature[1]
            word.append(Morph(surface,base,pos,pos1))
        if d in 'EOS' and word != []:
            sentence.append(word)
            word = []
    return sentence

def main():
    with open('./data/neko.txt.cabocha',mode='r') as fr:
        r = fr.read()
    morph = word_analysis(r)
    for m in morph[3]:
        #print(m.get_morph())
        print(m)

if __name__ == "__main__":
    main()

#他の回答
# init で使うなら宣言しなくていい
#__str__() は出力用? らしい
#    def __str__(self):
#        '''オブジェクトの文字列表現'''
#        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
#            .format(self.surface, self.base, self.pos, self.pos1)
#

