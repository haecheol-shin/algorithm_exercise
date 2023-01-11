import sys, heapq

n, k = map(int, sys.stdin.readline().split())
jewelry = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

jewelry.sort()
bags.sort()
tmp = []
result = 0

for bag in bags:
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(tmp, -jewelry[0][1])
        heapq.heappop(jewelry)
    
    if tmp:
        result += heapq.heappop(tmp)
    elif not jewelry:
        break

print(-result)