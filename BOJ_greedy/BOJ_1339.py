import sys

n = int(sys.stdin.readline())
wordlist = []

for i in range(n):
    wordlist.append(sys.stdin.readline())

for i in range(0,n,-1): # 배열에서 가장 긴 단어를 찾으면 맨 끝에 넣는다
    max = wordlist[0]
    if (len(max)<len(wordlist[i])):
        max = wordlist[i]
