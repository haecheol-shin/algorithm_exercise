from __future__ import barry_as_FLUFL


a = int(input())
sum = 0

for i in range(a+1):
    sum += i
    if (sum>=a):
        print(i)
        break