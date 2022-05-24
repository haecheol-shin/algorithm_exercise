from unittest import result


n = int(input())
stack = []

for i in range(n):
    inputNum = int(input())
    if inputNum==0 and len(stack)!=0:
        stack.pop()
    
    else:
        stack.append(inputNum)

result = 0
for i in stack:
    result = result + i

print(result)