from calendar import c
import sys
from collections import deque

n = int(sys.stdin.readline())

deque = deque()
for i in range(n):
    testCase = list(map(int, sys.stdin.readline().split()))

    priority = list(map(int, sys.stdin.readline().split()))

    for j in priority:
        deque.append(j)

    count = 0
    while(True):
        if max(deque)==deque[0]:
            count = count + 1
            deque.popleft()

        else:
            deque.append(deque.popleft())

        if testCase[1]==count:
            break

    # 우선순위가 같은 경우가 해결되지 않음.
    
print(count)
    
