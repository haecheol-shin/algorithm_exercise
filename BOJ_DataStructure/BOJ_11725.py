import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [0] * (n+1)

q = deque([1])
visited[1] = 0

while q:
    # 방문하지 않은 곳 부터 순차적으로 방문하고
    # 방문한 곳은 visited = 1로