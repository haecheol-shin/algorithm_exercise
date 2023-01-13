import sys

N = int(sys.stdin.readline()) ; arr = []

for _ in range(N):
    arr.append(list(map(str, sys.stdin.readline().split())))
arr.sort(key=lambda x : str(x[0])) ## 4번조건
arr.sort(key=lambda x:int(x[3]), reverse=True) ## 3번조건
arr.sort(key = lambda x : int(x[2])) ## 2번조건
arr.sort(key = lambda x: int(x[1]), reverse = True) ## 1번조건


for i in arr :
    print(i[0])