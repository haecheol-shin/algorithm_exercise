# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

import sys

# 사용자 입력
sentence = sys.stdin.readline().rstrip()
commandCount = int(sys.stdin.readline())

# 커서 기준으로 문자열을 나눔
leftSentence = list(sentence)
rightSentence = []

# 명령어 개수만큼 입력받음
for i in range(commandCount):
    command = sys.stdin.readline()
    commandList = list(command.split())
    
    if commandList[0]=='L':
        if len(leftSentence)!=0:
            rightSentence.append(leftSentence.pop())
        
        else:
            pass
    
    elif commandList[0]=='D':
        if len(rightSentence)!=0:
            leftSentence.append(rightSentence.pop())
        
        else:
            pass

    elif commandList[0]=='B':
        if len(leftSentence)!=0:
            leftSentence.pop()

        else:
            pass
    
    elif commandList[0]=='P':
        leftSentence.append(commandList[1])

    else:
        break

result = ''
for i in leftSentence:
    if i.isalpha():
        result = result + i
    else:
        pass

for i in rightSentence[::-1]:
    if i.isalpha(): 
        result = result + i
    else:
        pass

print(result)