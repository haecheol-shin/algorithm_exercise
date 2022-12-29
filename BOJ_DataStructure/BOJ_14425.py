import sys

n, m = map(int, sys.stdin.readline.input().split())
S = set()
for i in range(n):
    S.add(input())
answer = 0
for _ in range(m):
    t = input()
    if t in S:
        answer += 1
        
print(answer)
