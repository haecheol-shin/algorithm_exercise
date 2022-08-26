import sys
import heapq

n = int(sys.stdin.readline())
plusHeap = [] # 최소 힙
minusHeap = [] # 최대 힙

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(plusHeap) == 0 and len(minusHeap) == 0:
            print(0)
        
        else: # 최소 힙과 최대 힙의 절댓값을 비교하여 출력
            if len(plusHeap) == 0:
                print(heapq.heappop(minusHeap)[1])

            elif len(minusHeap) == 0:
                print(heapq.heappop(plusHeap))
            
            elif abs(plusHeap[0]) < abs(minusHeap[0][1]):
                print(heapq.heappop(plusHeap))

            elif abs(plusHeap[0]) > abs(minusHeap[0][1]):
                print(heapq.heappop(minusHeap)[1])

            elif abs(plusHeap[0]) == abs(minusHeap[0][1]):
                print(heapq.heappop(minusHeap)[1])

    elif x > 0: # x가 양수이면 양수 힙에 저장
        heapq.heappush(plusHeap, x)

    else: # x가 음수이면 음수 힙에 저장
        heapq.heappush(minusHeap, (-x, x))
