letters = 'abcdefghijklmnopqrstuvwxyz'
dic = {}

for ch in letters: 
    dic[ch] = 0

for s in input(): 
    dic[s] += 1

print(' '.join(map(str, dic.values())))