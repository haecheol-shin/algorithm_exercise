import math

a, r, n = input().split()

a = int(a)
r = int(r)
n = int(n)

answer = int(a*math.pow(r, (n-1)))

print(answer)