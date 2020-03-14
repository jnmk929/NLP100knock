#41. 係り受け解析結果の読み込み（文節・係り受け）
#40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素(Morphオブジェクト)の
#リスト(morphs),係り先文節インデックス番号(dst)係り元文節インデックス番号の
#リスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，
#１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．

from collections import defaultdict

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def get_surface(self):
        return self.surface

    def __str__(self):
        return 'surface:{}\tbase:{}\tpos:{}\tpos1:{}'.format(self.surface,self.base,self.pos,self.pos1)

class Chunk:
    def __init__(self,dist):
        self.dist = dist
        self.morphs = []
        self.srcs = []
    
    def set_marphs(self,morphs):
        self.morphs.append(morphs)
    
    def set_srcs(self,srcs):
        self.srcs = srcs
    
    def __str__(self):
        s = ''
        for morph in self.morphs:
            s += ''.join(morph.get_surface())
        return 'surface:{}\tdist:{}\tsrcs:{}'.format(s,self.dist,','.join(self.srcs))

def sentence_analysis(cabocha):
    analysis = []
    morph_list = []
    srcs_dict = defaultdict(list)
    for line in cabocha.split('\n'):
        if len(line) > 0 and '*' == line[0]:      #係り受け解析の処理 
            data = line.split(' ')
            chunk = Chunk(int(data[2][:-1]))
            morph_list.append(chunk)
            srcs_dict[int(data[2][:-1])].append(data[1])    #係り元の辞書を作る

        elif len(line) > 0 and not 'EOS' in line:     #形態素解析の処理
            surface = line.split('\t')[0]
            feature = line.split('\t')[1].split(',')   #特徴部分を抽出
            base = feature[6]
            pos = feature[0]
            pos1 = feature[1]
            chunk.set_marphs(Morph(surface,base,pos,pos1))
  
        if 'EOS' in line and morph_list != []:
            for i,morph in enumerate(morph_list):   #係り元のデータ挿入
                if i in srcs_dict.keys():
                    morph.set_srcs(srcs_dict[i])
            srcs_dict.clear()
            analysis.append(morph_list)
            morph_list = []
    return analysis

def main():
    with open('./data/neko.txt.cabocha',mode='r') as fr:
        r = fr.read()
    analysis_data = sentence_analysis(r)

    for i,data in enumerate(analysis_data,1):
        for sentence in data:
            if i == 8:
                print(sentence)

if __name__ == "__main__":
    main()

