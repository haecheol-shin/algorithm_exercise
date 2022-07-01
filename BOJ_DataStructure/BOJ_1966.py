import sys
from collections import deque

n = int(sys.stdin.readline())

deque = deque()

for i in range(n):
    testCase = list(map(int, sys.stdin.readline().split()))

    priority = list(map(int, sys.stdin.readline().split()))

    index = [ i for i in range(len(testCase[0]))]

    for j in priority:
        deque.append(j)

    count = 0
    while(True):
        while deque:
            if priority[0] == max(priority):    # 나머지 문서들보다 중요도가 더 높은 문서가 없다면
                count += 1
                if index[0] == 'target':
                    print(count)
                    break
                deque.pop(0)
                index.pop(0)
            else:
                deque.append(priority.pop(0))
                index.append(index.pop(0))
    
    # 찾고자 하는 값의 위치를 저장할 변수 1개
    # 찾고자 하는 값이 중복으로 여러 개 있는 경우 -> 그 값만 형변환해서 type검사를 해서 찾아낸다
