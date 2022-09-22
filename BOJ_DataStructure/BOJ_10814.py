import sys

n = int(sys.stdin.readline().rstrip())

memberList = []
for i in range(n):
    member = tuple(sys.stdin.readline().rstrip().split())
    memberList.append(member)

memberList.sort(key = lambda x: x[0])

for i in range(n):
    print(memberList[i][0], memberList[i][1])