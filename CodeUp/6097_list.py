a = [] # 빈 배열생성

w, h = map(int, input().split()) # W가 가로, h가 세로

for i in range(w):
    a.append([])
    for j in range(h):
        a[i].append(0) # w x h 크기의 배열 생성

n = int(input()) # n이 막대의 개수

for _ in range(n):
    l, d, x, y = map(int, input().split()) # d가 0이면 가로방향 1이면 세로방향

    for i in range(l):
        if (d==1):
            a[x-1+i][y-1] = 1
        
        else:
            a[x-1][y-1+i] = 1

for i in range(w):
    for j in range(h):
        print(a[i][j], end=' ')
    print()