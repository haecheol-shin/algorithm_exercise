import sys

t = int(sys.stdin.readline.input())
for _ in range(t):
    n = int(input())
    humans = sorted([list(map(int,input().rsplit())) for _ in range(n)])

    print(humans)

    compare = humans[0][1]
    count = 0
    for i in range(1,n):
        target = humans[i][1]
        compare = min(compare, target)
        if compare < target:
            count += 1
    
    print(n-count)