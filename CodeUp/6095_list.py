a=[]

for i in range(19):
    a.append([])
    for j in range(19):
        a[i].append(0)

n = int(input())

for i in range(n):
    x,y = map(int, input().split())

    for i in range(19):
        for j in range(19):
            if (i==(x-1) and j==(y-1)):
                a[i][j] = 1

for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print()