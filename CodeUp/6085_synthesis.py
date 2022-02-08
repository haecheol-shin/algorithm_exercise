a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(format(a*b*c/8/1024/1024, ".2f"), "MB")