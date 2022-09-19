import sys

num = list(map(int, sys.stdin.readline().rstrip().split()))

nList = []
mList = []
result = []

for i in range(num[0]):
    name = sys.stdin.readline().rstrip()
    nList.append(name)
nList = set(nList)

for i in range(num[1]):
    name = sys.stdin.readline().rstrip()
    mList.append(name)
mList = set(mList)

result = list(nList&mList)
result.sort()
print(len(result))
print('\n'.join(result))