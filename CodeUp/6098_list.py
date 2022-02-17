a = []

for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for i in range(10):
    a[i] = list(map(int, input().split()))

x, y = int(1)

break2 = False
for i in range(1,10):
    for j in range(1,10):
        if (a[x][y]==0):
            a[x][y] = 9
        
        elif (a[x][y]==2):
            a[x][y] = 9


        else:
            a[i][j] = 9
            break2 = True
            break
    
    if(break2==False):
        break
    
for i in range(10):
    for j in range(10):
        print(a[i][j], end=" ")
    print()
