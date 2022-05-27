
n = int(input()) # 탑의 개수
towerList = input().split()
print(towerList)

towerList.reverse()
stack = []
result = []
for i in range(len(towerList)):
    if len(stack)==0:
        stack.append(int(towerList[i]))
    
    elif int(stack[-1])<int(towerList[i]):
        result.append(n-i)
        for tower in stack:
            stack.pop()
            result.append(n-i)

    else:
        stack.append(int(towerList[i]))

    if i==len(towerList)-1:
        for _ in stack:
            result.append(0)

# 역순으로 출력 바꾸고, result 값이 하나씩 밀리는 느낌
print(result)