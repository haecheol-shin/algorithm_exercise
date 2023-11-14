import sys
from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(sys.stdin.readline()))

for height in combinations(heights, 7):
    if sum(list(height)) == 100:
        for i in sorted(list(height)):
            print(i)
        break

# 9C7 -> 7중 for문으로 풀어야 하지만
# 9C2 -> 2중 for문으로 풀 수 있다.