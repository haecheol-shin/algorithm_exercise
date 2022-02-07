a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)

print(a*b*c)