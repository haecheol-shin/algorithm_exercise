# 출력초과 뜸

def tower():
    n = int(input()) # 탑의 개수
    towerList = input().split()

    towerList.reverse()
    stack = []
    result = []
    for i in range(len(towerList)):
        if len(stack)==0:
            stack.append(int(towerList[i]))
        
        elif int(stack[-1])<int(towerList[i]):
            for _ in range(len(stack)):
                stack.pop()
                result.append(n-i)
            stack.append(int(towerList[i]))

        else:
            stack.append(int(towerList[i]))

    for _ in stack:
        result.append(0)

    result.reverse()

    flag = 0
    for i in range(len(result)):
        flag = flag + result[i]
        if i==len(result)-1:
            if flag==0:
                result.clear()
                return result
            else:
                return result

if __name__=="__main__":
    result = tower()
    if len(result)==0:
        print(0)
    else:
        for i in result:
            print(i, end=' ')

