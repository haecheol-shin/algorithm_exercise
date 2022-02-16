a = []

for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for i in range(10):
    a[i] = list(map(int, input().split()))

for i in range(1,10):
    for j in range(1,10):
        if (a[j+1][i]==1 or a[j+1][i]==2):
            i += 1
            break
        else:
            a[i][j] = 9

for i in range(10):
    for j in range(10):
        print(a[i][j], end=" ")
    print()
