a=[]

for i in range(19):
    a.append([])
    for j in range(1,19):
        a[i].append(0)

n = int(input())

for i in range(n):
    x,y = input().split()

    for i in range(1,20):
        for j in range(1,20):
            if (i==x and j==y):
                a[i][j] = 1

for i in range(20):
    for j in range(20):
        print(a[i][j], end=' ')
    print()