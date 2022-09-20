import sys

n = int(sys.stdin.readline().rstrip())

memberList = []
for i in range(n):
    member = tuple(sys.stdin.readline().rstrip().split())
    if i==0:
        memberList.append(member)

    elif member[0] < memberList[0][0]:
        memberList.insert(0, member)

    else:
        for j in range(len(memberList)):
            if memberList[j][0] <= member[0]:
                pass

            elif memberList[j][0] > member[0]:
                memberList.insert(j, member)
                break

            if j==len(memberList)-1:
                memberList.append(member)

for i in range(n):
    print(memberList[i][0], memberList[i][1])

    # 시간 초과