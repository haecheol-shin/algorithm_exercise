# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys
n = int(sys.stdin.readline())
nList = list(map(int, sys.stdin.readline().split()))
nList.sort()

m = int(sys.stdin.readline())
mList = list(map(int, sys.stdin.readline().split()))

def binary(l, nList, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == nList[m]:
        return 1
    elif l < nList[m]:
        return binary(l, nList, start, m-1)
    else:
        return binary(l, nList, m+1, end)

for l in mList:
    start = 0
    end = len(nList)-1
    print(binary(l,nList,start,end))