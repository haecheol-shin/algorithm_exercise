a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)

print(format(a*b*c*d/8/1024/1024 , ".1f"), "MB")