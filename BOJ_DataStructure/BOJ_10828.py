import sys

n = int(sys.stdin.readline()) # 명령 개수

stack = [] # 수를 저장하는 stack
userCommandList = [] # 유저의 명령을 저장하는 list

for i in range(n): # 명령 개수 만큼 반복
    userCommand = sys.stdin.readline()
    userCommandList = list(userCommand.split()) # push가 입력되는 경우 push와 수를 공백단위로 구별
    if (userCommandList[0]=='push'):
        stack.append(userCommandList[1]) # 수를 append()로 추가

    elif (userCommandList[0]=='top'):
        if (len(stack)==0): # 스택에 아무것도 없다면 -1 출력
            print(-1)
        else:
            print(stack[-1]) # 인덱스를 -1로 설정해서 스택의 top을 출력
    
    elif (userCommandList[0]=='size'): 
        print(len(stack)) # len()으로 size출력

    elif (userCommandList[0]=='pop'):
        if (len(stack)==0): # pop할게 없다면 -1 출력
            print(-1)
        else:
            print(stack.pop()) # pop()으로 pop출력
        
    elif(userCommandList[0]=='empty'):
        if (len(stack)==0): # len()으로 스택이 비어있는지 확인
            print(1)
        else:
            print(0)
