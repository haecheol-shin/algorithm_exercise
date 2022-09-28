import sys


def search(start, end):
    h = end - start # 나무 톱 높이
    sum = 0 # 자른 나무 길이의 합
    for i in range(n):
        if height[i]-h > 0:
            sum += height[i] - h
    
    if sum > m:
        h = h + ((h+end) // 2)
        search(h, end)
    
    elif sum < m:
        h = h//2
        search(h, end)

    else:
        print(h)
        return
        

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    height = list(map(int, sys.stdin.readline().rstrip().split()))

    height.sort()
    search(0, height[-1])