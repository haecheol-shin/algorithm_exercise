import sys
import heapq

n = int(sys.stdin.readline())

minHeap = [] # 최소 힙
maxHeap = [] # 최대 힙

for i in range(n):
    num = int(sys.stdin.readline())

    if len(minHeap)==0 and len(maxHeap)==0:
        middle = num

    if middle < num:
        heapq.heappush(minHeap, num)

    else:
        heapq.heappush(maxHeap, (-num, num))

    if len(minHeap)-len(maxHeap)==2:
        x = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, (-x, x))

    if len(minHeap)-len(maxHeap)==-2:
        x = heapq.heappop(maxHeap)[1]
        heapq.heappush(minHeap, x)
    
    if len(minHeap)==0:
        middle = maxHeap[0][1]

    else:
        middle = minHeap[0]

    if len(maxHeap)==0:
        print(minHeap[0])

    elif len(minHeap)-len(maxHeap) == 1:
        print(minHeap[0])

    else:
        print(maxHeap[0][1])

    