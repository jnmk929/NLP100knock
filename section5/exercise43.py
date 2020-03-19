#43. 名詞を含む文節が動詞を含む文節に係るものを抽出
#名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
# ただし，句読点などの記号は出力しないようにせよ．

from collections import defaultdict

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def get_surface(self):
        return self.surface
    
    def get_pos(self):
        return self.pos

    def __str__(self):
        return 'surface:{}\tbase:{}\tpos:{}\tpos1:{}'.format(self.surface,self.base,self.pos,self.pos1)

class Chunk:
    def __init__(self,dst):
        self.dst = dst
        self.morphs = []
        self.srcs = []
    
    def add_marphs(self,morphs):
        self.morphs.append(morphs)
    
    def set_srcs(self,srcs):
        self.srcs = srcs
    
    def get_dst(self):
        return self.dst
    
    def get_all_surface(self):
        surfaces = []
        for m in self.morphs:
            surface = m.get_surface() 
            if not surface in surfaces:
                surfaces.append(m.get_pos())
        return surfaces
    
    def get_morph(self,pos=''):
        morph = ''
        for m in self.morphs:
            if pos == '':
                morph += ''.join(m.get_surface())
            else:
                if pos != m.get_pos():
                    morph += ''.join(m.get_surface())
        return morph

    def __str__(self):
        morph = self.get_morph()
        return 'surface:{}\tdist:{}\tsrcs:{}'.format(morph,self.dist,','.join(self.srcs))

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
            chunk.add_marphs(Morph(surface,base,pos,pos1))
  
        if 'EOS' in line and morph_list != []:
            for i,morph in enumerate(morph_list):   #係り元のデータ挿入
                if i in srcs_dict.keys():
                    morph.set_srcs(srcs_dict[i])
            srcs_dict.clear()
            analysis.append(morph_list)
            morph_list = []
    return analysis

def print_phrase(analysis_data):
    for data in analysis_data:
        for chunk in data:
            dist = chunk.get_dst()
            morph = chunk.get_morph('記号')
            if dist != -1 and morph != '':
                print('{}\t{}'.format(morph,data[dist].get_morph('記号')))

def print_noun2verb(analysis_data):
    for data in analysis_data:
        for chunk in data:
            dst = chunk.get_dst()
            morph = chunk.get_morph('記号')
            if dst != -1 and morph != '':
                dst_s = chunk.get_all_surface()
                prior = data[dst].get_morph('記号')
                srcs_s = data[dst].get_all_surface()
                if '名詞' in dst_s and '動詞' in srcs_s:
                    print('{}\t{}'.format(morph,prior))

def main():
    with open('./data/neko.txt.cabocha',mode='r') as fr:
        r = fr.read()
    analysis_data = sentence_analysis(r)
    print_noun2verb(analysis_data)


if __name__ == "__main__":
    main()

