a = []

for i in range(19):
    a.append([])
    for j in range(19):
        a[i].append(0)

for i in range(19):
    a[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for i in range(19):
        for j in range(19):
            if (i==(x-1)):
                if (a[x-1][j]==0):
                    a[x-1][j]=1
                else:
                    a[x-1][j]=0

            if (j==(y-1)):
                if (a[i][y-1]==0):
                    a[i][y-1]=1
                else:
                    a[i][y-1]=0           


for i in range(19):
    for j in range(19):
        print(a[i][j], end=' ')
    print()