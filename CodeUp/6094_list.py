from posixpath import split


n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

result = a[0]

for i in range(1, n):
    if (result>a[i]):
        result = a[i]
        

print(result)