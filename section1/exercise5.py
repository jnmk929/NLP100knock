#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
#この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

str = 'I am an NLPer'
word = str.split(' ')

def n_gram(list,n):
    gram = []
    for i in range(len(list) - n + 1):
        gram.append(list[i:i+n])    
    return gram

if __name__ == "__main__":
    print(n_gram(str,2))
    print(n_gram(word,2))