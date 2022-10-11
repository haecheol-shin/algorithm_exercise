import sys 

n = int(sys.stdin.readline())

numCountList = [0] * 10000

for i in range(n):
    num = int(sys.stdin.readline())
    numCountList[num-1] += 1

for i in range(n):
    count[int(sys.stdin.readline())] += 1

    max_value = 0
    for i in range(n-1):
        max_value = max(max_value, count[i])
        if count[i+1] != 0:
            count[i+1] += max_value

    before = 0
    for i in range(1,n+1):
        before = max(before, count[i-1])
        if count[i] != 0:
            index = count[i]
        while index-before > 0:
            lst[index-1] = i
            index -= 1

    lst = list(map(str,lst))
    print("\n".join(lst))
