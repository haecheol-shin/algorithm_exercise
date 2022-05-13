import sys

n = int(sys.stdin.readline()) # 피연산자 개수
stack = [] # 피연산자를 저장할 스택
alphaSentence = sys.stdin.readline() # 후위 표기식
num = [] # 피연산자의 숫자를 저장하는 배열
digitSentence = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

count = 0
for i in range(len(alphaSentence)): # 후위 표기식의 문자를 숫자로 바꿈
    if alphaSentence[i].isalpha() == True:
        digitSentence.append(num[count])
        count += 1

    else:
        digitSentence.append(alphaSentence[i])

digitSentence.pop() # 맨 뒤 널 문자를 pop

i = 0
while():
    stack.append(digitSentence[i])

    if(i>=2): 
        if(str(stack[i-2]).isdigit()==True and str(stack[i-1]).isdigit()==True and str(stack[i]).isdigit()==False):
            if (stack[i]=='+'):
                stack[i-2] = stack[i-2] + stack[i-1]
                stack.pop()
                stack.pop()
                i -= 2

            elif (stack[i]=='-'):
                stack[i-2] = stack[i-2] - stack[i-1]
                stack.pop()
                stack.pop()
                i -= 2

            elif (stack[i]=='*'):
                stack[i-2] = stack[i-2] * stack[i-1]
                stack.pop()
                stack.pop()
                i -= 2
                
            elif (stack[i]=='/'):
                stack[i-2] = stack[i-2] / stack[i-1]
                stack.pop()
                stack.pop()
                i -= 2

            else:
                break
        
        else:
            pass
    else:
        pass

    i += 1

    # 무한루프를 빠져나올 조건문 필요

print(stack)