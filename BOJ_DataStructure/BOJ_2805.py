import sys
   
n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(height)
while(start <= end):
    mid = (start + end) // 2

    result = 0
    for i in height:
        if i > mid:
            result += i - mid
        if result >= m:
            break

    if result < m:
        end = mid - 1

    else:
        start = mid + 1

print(end)      