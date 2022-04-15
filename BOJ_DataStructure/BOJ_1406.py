# L: 커서를 왼쪽으로 한칸 옮김
# D: 커서를 오른쪽으로 한칸 옮김
# B: 커서 왼쪽에 있는 문자를 삭제
# P ?: ?라는 문자를 커서 왼쪽에 추가함

# deque 를 사용해서 해결해야함

import sys

sentence = list(sys.stdin.readline()) # 초기 문자열
sentence.pop() # 널문자 제거
n = int(sys.stdin.readline()) # 명령 횟수
pointer = len(sentence)

for i in range(n):
    userCommand = list(sys.stdin.readline().split())
    
    if (userCommand[0]=='P'):
        sentence.insert(pointer, userCommand[1])
        pointer += 1
    
    elif (userCommand[0]=='L'):
        if (pointer==0):
            pass
        else:
            pointer -= 1
    
    elif (userCommand[0]=='D'):
        if (pointer==len(sentence)):
            pass
        else:
            pointer += 1
    
    elif (userCommand[0]=='B'):
        if (pointer==0):
            pass
        else:
            del sentence[pointer-1]
            pointer -= 1
        
    else:
        break

print(''.join(i for i in sentence))