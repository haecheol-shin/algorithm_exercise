import sys
from heapq import *

heap = []

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    if num == 0:
        if len(heap) == 0:
            print(0)

        else:
            if heap[0][1] == 0:
                print(-heappop(heap)[0])

            else:
                print(heappop(heap)[0])

    else:
        if num > 0:
            heappush(heap, (num, 1))
        else:
            heappush(heap, (-num, 0))
