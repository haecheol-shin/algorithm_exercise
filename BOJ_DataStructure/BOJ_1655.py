import sys
import heapq

n = int(sys.stdin.readline())

minHeap = [] # 최소값
midHeap = [] # 중간값
maxHeap = [] # 최댓값

for i in range(n):
    num = int(sys.stdin.readline())
    
    if len(minHeap) == 0:
        heapq.heappush(minHeap, num)

    elif len(midHeap) == 0:
        heapq.heappush(midHeap, num)

    elif len(maxHeap) == 0:
        heapq.heappush(maxHeap, num)

    if minHeap[0]

    # 중간값을 가진 최소힙에서 최솟값을 반환하는 것으로 답을 한다.
    # 숫자를 넣을 때 어떤 힙에 들어가야 될지 처리하는 과정이 필요
    # 최소 힙과 최대 힙을 섞으면 가능할수도
