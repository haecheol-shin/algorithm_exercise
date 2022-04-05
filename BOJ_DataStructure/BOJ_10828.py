import sys

n = int(sys.stdin.readline()) # 명령 개수

stack = []
userCommandList = []
for i in range(n):
    userCommand = sys.stdin.readline()
    userCommandList = list(userCommand.split())
    if (userCommandList[0]=='push'):
        stack.append(userCommandList[1])

    elif (userCommandList[0]=='top'):
        if (len(stack)==0):
            print(-1)
        else:
            print(stack[-1])
    
    elif (userCommandList[0]=='size'):
        print(len(stack))

    elif (userCommandList[0]=='pop'):
        if (len(stack)==0):
            print(-1)
        else:
            print(stack.pop())
        
    elif(userCommandList[0]=='empty'):
        if (len(stack)==0):
            print(1)
        else:
            print(0)
