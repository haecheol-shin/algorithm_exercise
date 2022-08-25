import sys
import heapq

n = int(sys.stdin.readline())
plusHeap = []
minusHeap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(plusHeap) == 0 and len(minusHeap) == 0:
            print(0)
        
        else: # 최소 힙과 최대 힙의 절댓값을 비교하여 출력
            if plusHeap[0] > -minusHeap[0]:
                print(heapq.heappop(plusHeap))

            else:
                print(heapq.heappop(minusHeap))

    elif x > 0: # x가 양수이면 최소 힙에 저장
        heapq.heappush(plusHeap, x)

    else: # x가 음수이면 최대 힙에 저장
        heapq.heappush(minusHeap, x)
