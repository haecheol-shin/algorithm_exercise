# L: 커서를 왼쪽으로 한칸 옮김
# D: 커서를 오른쪽으로 한칸 옮김
# B: 커서 왼쪽에 있는 문자를 삭제
# P ?: ?라는 문자를 커서 왼쪽에 추가함

import sys

sentence = sys.stdin.readline() # 초기 문자열
sentence = '.'+'.'.join(sentence)
n = int(sys.stdin.readline()) # 명령 횟수
userCommand = []
pointer = -1

for i in range(n):
    userCommand.append(sys.stdin.readline().split())
    
    if (userCommand[0]=='P'):
        push(userCommand[1])
    elif (userCommand[0]=='L'):
        left()
    elif (userCommand[0]=='D'):
        right()
    elif (userCommand[0]=='B'):
        delete()
    else:
        break
        
def push(letter):

def left():

def right():

def delete():
