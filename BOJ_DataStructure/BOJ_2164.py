import sys
from collections import deque

n = int(sys.stdin.readline())
card = deque() # 데크를 선언할 때는 함수처럼 쓴다. 힙 사용과는 차이가 있다

for i in range(n, 0, -1):
    card.append(i)

while(len(card)!=1):
    card.pop()
    card.appendleft(card.pop())

print(*card) # deque 안의 원소만 출력할때는 *을 붙인다.

# deque는 양 끝 원소에 대한 접근은 O(1)이다.