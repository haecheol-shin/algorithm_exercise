a = []

for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for i in range(10):
    a[i] = list(map(int, input().split()))

y = 0
break2 = True

for i in range(1,10):
    for j in range(1,10):
        
        j = y+1


        if (a[i][j]==0):
            a[i][j] = 9
        
        elif (a[i][j]==1):
            y = j
            break


        else:
            a[i][j] = 9
            break2 = False
            break
    
    if(break2==False):
        break
    
for i in range(10):
    for j in range(10):
        print(a[i][j], end=" ")
    print()
