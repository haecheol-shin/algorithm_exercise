import sys
from collections import deque

n, l = map(int, sys.stdin.readline().split())
arr = [*map(int, sys.stdin.readline().split())]
m = deque()
for i in range(n):
    tmp = arr[i]

    while m and m[-1] > tmp: m.pop()
    m.append(tmp)

    if i >= l and m[0] == arr[i-l]: m.popleft()
    print(m[0], end=' ')