import sys
from collections import deque

n = int(sys.stdin.readline())

deque = deque()
for i in range(n):
    testCase = list(map(int, sys.stdin.readline().split()))

    priority = list(map(int, sys.stdin.readline().split()))

    for j in priority:
        deque.append(j)

    priority[testCase[1]] = str(priority[testCase[1]])
    count = 0
    while(True):
        if max(deque)!=int(deque[0]):
            deque.append(deque.popleft)
        
        elif max(deque)==int(deque[0]):
            count = count + 1
            deque.popleft()

        elif max(deque)==int(deque[0]) and type(deque[0]) is str:
            count = count + 1
            break
    
    print(count)
    
    # 찾고자 하는 값의 위치를 저장할 변수 1개
    # 찾고자 하는 값이 중복으로 여러 개 있는 경우 -> 그 값만 형변환해서 type검사를 해서 찾아낸다
