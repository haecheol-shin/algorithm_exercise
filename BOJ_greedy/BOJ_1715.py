import sys
from queue import PriorityQueue

n = int(sys.stdin.readline()) # 카드 뭉치 개수
card_cnt = PriorityQueue()

for i in range(n):
    card_cnt.put(int(sys.stdin.readline()))

sum = 0

for i in range(n):

    if (card_cnt.qsize()==1): # 카드가 한 묶음으로 줄면 종료
        break
    
    addNum = card_cnt.get() + card_cnt.get() # get은 삭제하면서 반환을 한다
    sum += addNum
    card_cnt.put(addNum) # 우선순위큐에서 get과 put은 O(n)이다

print(sum)