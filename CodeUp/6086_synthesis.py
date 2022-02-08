a = int(input())
sum = 0

for i in range(a+1):
    if (sum<a):
        sum += i
    else:
        break

print(sum)

