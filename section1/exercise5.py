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

def n_gram2(string,select,n):
    #単語n-gram
    gram = []
    if select == 0:
        word = string.split(' ')
        for i in range(len(word)-n+1):
            gram.append(word[i:i+n])
    #文字n-gram
    if select == 1:
        for i in range(len(string)-n+1):
            gram.append(string[i:i+n])

    return gram



if __name__ == "__main__":
    #print(n_gram(str,2))
    #print(n_gram(word,2))
    print(n_gram2(str,0,2))
    print(n_gram2(str,1,2))