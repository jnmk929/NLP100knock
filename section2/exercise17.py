#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

pre = []
rfile = './hightemp.txt'
with open(rfile,mode='r',encoding='utf_8') as f:
    for line in f:
        #line = line.replace('\n','')
        line = line.split('\t')
        if not line[0] in pre:
            pre.append(line[0])
print(pre)

#他の回答
#配列か集合型かの違い
#fname = 'hightemp.txt'
#with open(fname,'r',encoding='utf_8') as data_file:

 #   set_ken = set()
 #   for line in data_file:
 #       cols = line.split('\t')
 #       set_ken.add(cols[0])

#for n in set_ken:
 #   print(n)

'''
#!/bin/sh

# 先頭カラムを切り出し、ソート、重複除去
cut --fields=1 hightemp.txt | sort | uniq > result_test.txt

# Pythonのプログラムで実行、diffで比較するためにソート
python main.py | sort > result.txt

# 結果の確認
diff --report-identical-files result.txt result_test.txt
 '''